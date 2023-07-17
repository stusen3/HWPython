#  📌Напишите следующие функции:
#        ○ Нахождение корней квадратного уравнения
#        ○ Генерация csv файла с тремя случайными числами в каждой строке. 
#          100-1000 строк.
#        ○ Декоратор, запускающий функцию нахождения корней квадратного 
#          уравнения с каждой тройкой чисел из csv файла.
#        ○ Декоратор, сохраняющий переданные параметры и результаты работы 
#          функции в json файл.
import csv
import json
import math
import os.path
from random import randint as rd
from typing import Callable


def write_csv(function: Callable):
    write_coef_csvfile()

    def wrapper():
        with open('coef_quadratic.csv', 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for coef in data:
                if coef and coef[0] != 0:
                    function(*coef)

    return wrapper


def write_jsonfile(func: Callable):
    result = {}
    if os.path.exists('rwf.json'):
        with open('rwf.json', 'r', encoding='UTF-8') as file:
            result = json.load(file)
    else:
        with open('rwf.json', 'w', encoding='UTF-8') as file:
            json.dump(result, file)
    def wrapper(*args):
        roots = func(*args)
        solve_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': roots}
        result = solve_dict
        with open('rwf.json', 'w', encoding='UTF-8', ) as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
        return roots
    print("Решение записано в файл rwf.json")
    return wrapper


def write_coef_csvfile():
    with open('coef_quadratic.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(rd(2, 5)):
            writer.writerow([rd(-1000, 1000), rd(-1000, 1000), rd(-1000, 1000)])


@write_csv
@write_jsonfile
def quadratic(*args) -> tuple | float | None:
    a, b, c = args
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif disc == 0:
        x = -b / (2 * a)
        return round(x, 2)


quadratic()