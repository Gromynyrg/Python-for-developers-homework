from threading import Thread
import time


def square_of_nums(number_range: int = 10):
    """
    Функция считает и выводит квадраты чисел от 1 до N

    :param number_range: Число до которого выводить квадраты
    """
    for i in range(1, number_range + 1):
        print(f'{i}^2 = {i ** 2}')


def cubes_of_nums(number_range: int = 11):
    """
    Функция считает и выводит кубы чисел от 1 до N

    :param number_range: Число до которого выводить кубы
    """
    for i in range(1, number_range):
        print(f'{i}^3 = {i ** 3}')


def print_numbers():
    """
    Функция выводит числа от 1 до 10 с паузой в 1 секунду
    """
    for i in range(1, 11):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    task_number = input("Please, enter task number (1..4): ")
    if task_number == "1":
        square_thread = Thread(target=square_of_nums)
        cube_thread = Thread(target=cubes_of_nums)

        square_thread.start()
        cube_thread.start()

        square_thread.join()
        cube_thread.join()
    elif task_number == "2":
        thread_list = []
        for i in range(5):
            new_thread = Thread(target=print_numbers)
            thread_list.append(new_thread)
            new_thread.start()
        for thread in thread_list:
            thread.join()
    elif task_number == "3":
        pass
    elif task_number == "4":
        pass
    else:
        print("Error: Invalid key! Try another next time")

