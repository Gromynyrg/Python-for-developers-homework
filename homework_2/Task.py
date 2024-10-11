def copy_to_new_file(filename_target: str, filename_copy: str):
    """
    Функция для копирования данных из файла в новый файл

    :param filename_target: Путь до файла из которого будут скопированы данные
    :param filename_copy: Путь до файла в который будут скопированы данные
    """
    with open(filename_target, 'r') as file_1, open(filename_copy, 'w') as file_2:
        for line in file_1:
            file_2.write(line)


def calculate_cost_from_file(filename: str) -> float:
    """
    Функция для подсчета стоимости заказа из файла

    :param filename: Путь до файла с заказами
    :return: Сумма стоимости заказов
    """
    total_cost = 0.0
    with open(filename, 'r') as file:
        for line in file:
            position_data = line.split()
            order_cost = float(position_data[1]) * float(position_data[2])
            total_cost += order_cost
    print(total_cost)
    return total_cost


if __name__ == "__main__":
    task_number = input("Please, enter task number (1..4): ")
    function_for_tasks = {
        "1": copy_to_new_file('files/source.txt', 'files/destination.txt'),
        "2": calculate_cost_from_file('files/prices.txt'),
    }
    try:
        function_for_tasks[task_number]
    except KeyError as e:
        print("Error: Invalid key! Try another next time")
        print(f"Original error message: {str(e)}")
