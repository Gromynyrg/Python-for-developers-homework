def division_by_zero():
    a = int(input('Enter the first int number: '))
    b = int(input('Enter the second int number: '))
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print("Error: Division by zero!")
        print(f"Original error message: {str(e)}")


if __name__ == "__main__":
    task_number = input("Please, enter task number: ")
    function_for_tasks = {
        "1": division_by_zero,
    }
    function_for_tasks[task_number]()