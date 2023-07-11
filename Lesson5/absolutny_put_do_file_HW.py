# ФУНКЦИЯ РАЗДЕЛЕНИЯ (ПАПКА, ИМЯ, РАСШИРЕНИЕ)

# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os

string = "I:\PyCharm\pythonNewLesson\Lesson5\absolutny_put_do_file_HW.py"


def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension


print(f'Кортеж из трех элементов (путь, имя файла, расширение файла):  \n{fun(string)}')