from pydantic import BaseModel, EmailStr, Field, UUID4, field_validator
from uuid import uuid4


class BookNotAvailable(Exception):
    def __init__(self, message):
        super().__init__(message)


class Book(BaseModel):
    title: str
    author: str
    year: int
    available: bool = True
    categories: list[str]

    @field_validator('categories', mode='before')
    def validate_categories(cls, categories):
        if not categories:
            raise ValueError('Categories list should not be empty')
        else:
            for category in categories:
                if category not in ['Fiction', 'Classic', 'Non-Fiction', 'Fantastic', 'Thriller', 'Biography',
                                    'History', 'Mystery', 'Romance', 'Science', 'Self-Help', 'Travel', 'Horror',
                                    'Adventure', 'Humor', 'Philosophy', 'Psychology', 'Business', 'Economics',
                                    'Memoir', 'Poetry', 'Drama']:
                    raise ValueError(f'Invalid category: {category}')

        return categories


class User(BaseModel):
    name: str
    email: EmailStr
    membership_id: UUID4 = Field(default_factory=uuid4)


class Library(BaseModel):
    books: list[Book]
    users: list[User]

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def create_and_add_book(self, title: str, author: str, year: str, categories: list[str]) -> Book:
        new_book = Book(title=title, author=author, year=year, categories=categories)
        self.books.append(new_book)
        return new_book

    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None

    def is_book_borrow(self, title: str) -> bool:
        for book in self.books:
            if book.title == title and book.available:
                return False
        raise BookNotAvailable("Book not available, you can't borrow it")

    def borrow_book(self, title: str) -> None:
        if not self.is_book_borrow(title):
            book = self.find_book(title)
            book.available = False

    def total_books(self) -> int:
        return len(self.books)


if __name__ == '__main__':
    new_lib = Library(
        books=[
            Book(title='Book 1', author='Author 1', year=2022, categories=['Fiction', 'Classic']),
            Book(title='Book 2', author='Author 2', year=2021, categories=['Non-Fiction', 'Thriller']),
        ],
        users=[
            User(name='User 1', email='user1@example.com'),
            User(name='User 2', email='user2@example.com'),
        ]
    )
    new_lib.borrow_book(title='Book 1')
    print(new_lib.books)
    print(new_lib.total_books())
