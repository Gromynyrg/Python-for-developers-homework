def copy_to_new_file(filename_target: str, filename_copy: str):
    """
    Функция для копирования данных из файла в новый файл

    :param filename_target: Путь до файла из которого будут скопированы данные
    :param filename_copy: Путь до файла в который будут скопированы данные
    """
    with open(filename_target, 'r', encoding='UTF-8') as file_1, open(filename_copy, 'w', encoding='UTF-8') as file_2:
        for line in file_1:
            file_2.write(line)


def calculate_cost_from_file(filename: str) -> float:
    """
    Функция для подсчета стоимости заказа из файла

    :param filename: Путь до файла с заказами
    :return: Сумма стоимости заказов
    """
    total_cost = 0.0
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            position_data = line.split()
            order_cost = float(position_data[1]) * float(position_data[2])
            total_cost += order_cost
    print(total_cost)
    return total_cost


def get_words_count_from_file(filename: str) -> int:
    """
    Функция для подсчета кол-ва слов в файле

    :param filename: Путь до файла
    :return: Кол-во слов
    """
    word_count = 0
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            current_line = line.split()
            for word in current_line:
                if len(word) > 1 or len(word) == 1 and word.isalpha():
                    word_count += 1
    print(word_count)
    return word_count


def get_unique_rows_from_file(filename_target: str, filename_result: str):
    """
    Функция для записи всех уникальных строк в новый файл

    :param filename_target: Путь до файла со всеми строками
    :param filename_result: Путь до файла для уникальных строк
    """
    unique_rows = set()
    with open(filename_target, 'r', encoding='UTF-8') as file:
        for line in file:
            unique_rows.add(line.strip())
    with open(filename_result, 'w', encoding='UTF-8') as file:
        for row in unique_rows:
            file.write(f'{row}\n')


if __name__ == "__main__":
    task_number = input("Please, enter task number (1..4): ")
    if task_number == "1":
        copy_to_new_file('files/source.txt', 'files/destination.txt')
    elif task_number == "2":
        calculate_cost_from_file('files/prices.txt')
    elif task_number == "3":
        get_words_count_from_file('files/text_file.txt')
    elif task_number == "4":
        get_unique_rows_from_file('files/input.txt', 'files/unique_output.txt')
    else:
        print("Error: Invalid key! Try another next time")
