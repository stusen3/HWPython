# 📌Добавить к задаче строки документации и методы вывода
#    информации на печать.

# Задача 1
# Создайте класс 'Моя Строка', где:
# будут доступны все возможности str,
# дополнительно хранятся имя автора строки и время создания (time.time).

import time
class MyString(str):
    '''Класс str.'''

    def __new__(cls, text, nameAuthor):
        '''Метод new с дополнительными параметрами - text и nameAuthor.'''
        
        instance = super().__new__(cls, text)
        instance.nameAuthor = nameAuthor
        instance.t = time.time()
        instance.author = nameAuthor
        return instance

    def __str__(self):
        '''Метод строчного вывода экземпляра класса.'''
        
        return self + " " + f'{self.nameAuthor} {self.t}'


text = """Author comment"""
d = MyString(text, "Alex")
print(d.__dict__)
print(d.nameAuthor)
print(d.t)
print(d.upper())

help(d)
help(MyString)