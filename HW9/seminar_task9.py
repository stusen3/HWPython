# Задача 1

# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток.
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable


def ugaday_function(guess: int, attempts: int) -> Callable:  
    count = attempts
    val = -1

    def attempts_count():  
        nonlocal count
        nonlocal val
        while count > 0:
            count -= 1
            val = int(input("Попробуйте угадать число? "))
            if val == guess:
                return "Вы выиграли!"
        return "Количество попыток исчерпано! Вы не угадали(:"

    return attempts_count  


game = ugaday_function(5, 3) 
print(game())

# Задача 2

# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

# import random
# from typing import Callable
#
#
# def ugaday_function(fun: Callable) -> Callable:  
#
#     def wrapper(guess: int, attempts: int):  
#         guess = guess if 1 < guess < 100 else random.randint(1, 100)
#         attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)
#         return fun(guess, attempts)
#
#     return wrapper
#
#
# @ugaday_function  
# def attempts_count(guess: int, attempts: int):  
#     while attempts > 0:
#         attempts -= 1
#         val = int(input("Попробуйте угадать число? "))
#         if val == guess:
#             return "Вы выиграли!"
#     return "Количество попыток исчерпано!"
#
#
# print(attempts_count(150, 15))

# Задача 3

# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.

# import json
#
#
# def deco(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         filename = f'{func.__name__}.json'
#         dump_dict = {}
#         dump_dict["arguments"] = [*args]
#         for key, value in kwargs.items():
#             dump_dict[key] = value
#         dump_dict["result"] = result
#         json.dump(dump_dict, open(filename, 'a', encoding="utf-8"), indent=4)
#         return result
#
#     return wrapper
#
#
# @deco
# def sum_ever(x, y):
#     return x + y
#
#
# print(sum_ever(5, 10))
# print(sum_ever(y=3, x=20))

# Задача 4

# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

# from typing import Callable
#
# def counter(num: int):
#     def level_one(func: Callable):
#         cache = []
#
#         def wrapper(*args, **kwargs):
#             for _ in range(num):
#                 cache.append(func(*args, **kwargs))
#             return cache
#
#         return wrapper
#     return level_one
#
# @counter(5)
# def func(text: str):
#     return text.upper()
#
# print(func("Ура!"))

# Задача 5, 6 (Доработайте прошлую задачу, добавив декоратор wraps в каждый из декораторов.)

# Объедините функции из прошлых задач.
# Функцию-угадайку задекорируйте:
# декораторами для сохранения параметров,
# декоратором контроля значений и
# декоратором для многократного запуска.
# Выберите верный порядок декораторов.

# import json
# import random
# from typing import Callable
#
#
# def save_param_deco(func):                                            
#         result = func(*args, **kwargs)
#         filename = f'{func.__name__}.json'
#         dump_dict = {}
#         dump_dict["arguments"] = [*args]
#         for key, value in kwargs.items():
#             dump_dict[key] = value
#         dump_dict["result"] = result
#         json.dump(dump_dict, open(filename, 'a', encoding="utf-8"), indent=4, ensure_ascii=False)       
#         return result
#     return wrapper
#
#
# def param_control_deco(fun: Callable) -> Callable:                      
#
#    def wrapper(guess: int, attempts: int):
#        guess = guess if 1 < guess < 100 else random.randint(1, 100)
#        attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)
#        return fun(guess, attempts)
#
#    return wrapper
#
#
# def counter_deco(num: int):                                                  
#     def level_one(func: Callable):
#         cache = []
#
#         def wrapper(*args, **kwargs):
#             for _ in range(num):
#                 cache.append(func(*args, **kwargs))
#             return cache
#
#         return wrapper
#     return level_one
#
#
# # декорируемся в следующей последовательности:
#
# @counter_deco(1)                                                        
# @param_control_deco                                                   
# @save_param_deco                                                        
# def guess_game(guess: int, attempts: int):                              
#     while attempts > 0:
#         attempts -= 1
#         val = int(input("Попробуйте угадать число? "))
#         if val == guess:
#             return "Вы победили!"
#     return "Количество попыток исчерпано!"
#
#
# print(guess_game(5, 2))