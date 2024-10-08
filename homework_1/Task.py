import random as rnd


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


def type_error_exception():
    new_float_string = input("Please enter a float number: ")
    try:
        print(float(new_float_string))
    except ValueError as e:
        print("Error: Invalid input! Must be a number")
        print(f"Original error message: {str(e)}")


def index_out_of_range_exception():
    new_list = [rnd.randint(0, 10) for i in range(10)]
    index = int(input("Enter list element's index in range (0..9): "))
    try:
        print(f'In list [{new_list}] your element with index {index} is {new_list[index]}')
    except IndexError as e:
        print("Error: Index out of range!")
        print(f"Original error message: {str(e)}")


def math_and_sqrt_exception():
    answer = ''
    while answer.lower() not in ['y', 'n']:
        answer = input("Do you want to import module math? (y/n): ")
    try:
        if answer.lower() == "y":
            import math
            number = float(input("Enter the positive number: "))
            print(math.sqrt(number))
        else:
            raise ImportError("ImportError: you forgot to import module math")
    except ImportError as e:
        print("Error: Could not import module math")
        print(f"Original error message: {str(e)}")
    except ValueError as e:
        print("Error: Invalid input! Must be a positive number to get sqrt")
        print(f"Original error message: {str(e)}")


if __name__ == "__main__":
    task_number = input("Please, enter task number (1..6): ")
    function_for_tasks = {
        "1": division_by_zero_exception,
        "2": value_error_exception,
        "3": not_odd_positive_exception,
        "4": index_out_of_range_exception,
        "5": type_error_exception,
        "6": math_and_sqrt_exception,
    }
    try:
        function_for_tasks[task_number]()
    except KeyError as e:
        print("Error: Invalid key! Try another next time")
        print(f"Original error message: {str(e)}")
