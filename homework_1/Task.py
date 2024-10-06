class NotOddPositive(Exception):
    def __init__(self, message):
        super().__init__(message)


def division_by_zero_exception():
    a = int(input('Enter the first int number: '))
    b = int(input('Enter the second int number: '))
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print("Error: Division by zero!")
        print(f"Original error message: {str(e)}")


def value_error_exception():
    try:
        division_by_zero_exception()
    except ValueError as e:
        print("Error: Invalid input! Must be a number")
        print(f"Original error message: {str(e)}")


def sum_of_positive_odds(massive: list) -> int:
    sum_ods = 0
    for el in massive:
        if el % 2 == 0 or el < 0:
            raise NotOddPositive(f"Your list must contain only odd and positive numbers, but found {el}")
        else:
            sum_ods += el
    return sum_ods


def not_odd_positive_exception():
    numbers = list(map(int, input("Enter a list of positive odd numbers: ").split(' ')))
    try:
        print(sum_of_positive_odds(numbers))
    except NotOddPositive as e:
        print("Error: List must contain only odd and positive numbers")
        print(f"Original error message: {str(e)}")


if __name__ == "__main__":
    task_number = input("Please, enter task number: ")
    function_for_tasks = {
        "1": division_by_zero_exception,
        "2": value_error_exception,
        "3": not_odd_positive_exception,
    }
    function_for_tasks[task_number]()
