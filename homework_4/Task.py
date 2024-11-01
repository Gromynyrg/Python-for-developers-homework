class NotEnoughStock(Exception):
    def __init__(self, message):
        super().__init__(message)


class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock + quantity >= 0:
            self.stock += quantity
        else:
            raise NotEnoughStock("Stock cannot be less than 0")


class Order:
    def __init__(self, products: dict = None):
        if products is None:
            products = dict()
        self.products = products

    def add_product(self, product: Product, quantity: int):
        if product.stock >= quantity:
            product.update_stock(-1 * quantity)
            self.products[product] = quantity
        else:
            raise NotEnoughStock(f"Not enough stock for {product.name}")

    def calculate_total(self) -> float:
        total_cost = 0.0
        for product, quantity in self.products.items():
            total_cost += product.price * quantity
        return total_cost

    def remove_product(self, product: Product, quantity: int):
        if product in self.products:
            if self.products[product] > quantity:
                self.products[product] -= quantity
                product.update_stock(quantity)
            else:
                product.update_stock(self.products[product])
                self.products.pop(product)
        else:
            raise ValueError(f"Order does not contain {product.name}")


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(f"{product.name}: {product.price} gold, {product.stock} left")

    @staticmethod
    def create_order() -> Order:
        return Order()


if __name__ == '__main__':
    # Создаем магазин
    store = Store()

    # Создаем товары
    product1 = Product("Ноутбук", 1000, 5)
    product2 = Product("Смартфон", 500, 10)

    # Добавляем товары в магазин
    store.add_product(product1)
    store.add_product(product2)

    # Список всех товаров
    store.list_products()

    # Создаем заказ
    order = store.create_order()

    # Добавляем товары в заказ
    order.add_product(product1, 2)
    order.add_product(product2, 3)

    # Выводим общую стоимость заказа
    total = order.calculate_total()
    print(f"Общая стоимость заказа: {total}")

    # Проверяем остатки на складе после заказа
    store.list_products()

    # Удаляем товар из заказа
    order.remove_product(product1, 1)

    # Выводим общую стоимость заказа после удаления товара
    total = order.calculate_total()
    print(f"Общая стоимость заказа после удаления: {total}")
