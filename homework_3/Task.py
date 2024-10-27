from threading import Thread
import time
import asyncio
import multiprocessing
import math


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


async def calculate_square(num: int):
    """
    Функция вычисляет и выводит квадрат числа
    """
    await asyncio.sleep(1)
    print(f'{num}^2 - {num ** 2}')


async def create_async_calculate():
    numbers_list = [x for x in range(1, 11)]
    tasks = []
    for number in numbers_list:
        tasks.append(asyncio.create_task(calculate_square(number)))

    for task in tasks:
        await task


def calculate_factorial(num: int):
    """
    Функция вычисляет и выводит факториал числа

    :param num: Число целого типа
    """
    print(f'Factorial of {num} is {math.factorial(num)}')


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
        for j in range(5):
            new_thread = Thread(target=print_numbers)
            thread_list.append(new_thread)
            new_thread.start()
        for thread in thread_list:
            thread.join()

    elif task_number == "3":
        asyncio.run(create_async_calculate())

    elif task_number == "4":
        numbers = [x for x in range(110)]
        process_list = []
        for number in numbers:
            process_list.append(
                multiprocessing.Process(target=calculate_factorial, args=(number,))
            )
            process_list[-1].start()
        for process in process_list:
            process.join()

    else:
        print("Error: Invalid key! Try another next time")

