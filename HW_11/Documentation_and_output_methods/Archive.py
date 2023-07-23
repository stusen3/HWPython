# 📌Добавить к задаче строки документации и методы вывода
#    информации на печать.

#Задача 2
# Создайте класс 'Архив', который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов,
# list-архивы также являются свойствами экземпляра.

# Задача 3
# Добавьте к задачам 1 и 2 строки документации для классов.

# Задача 4
# Доработаем класс 'Архив' из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive():
    """Почему комментарии в самом классе? Потому что это документация ©Зухра"""

    _flag = None
    

    def __new__(cls, number, text):
        """"Функция заполняет архив старыми значениями."""

        if cls._flag == None:
            cls._flag = super().__new__(cls)
            cls._flag.archNumber = []
            cls._flag.archText = []
        elif cls._flag != None:
            cls._flag.archText.append(cls._flag.text)
            cls._flag.archNumber.append(cls._flag.number)
        return cls._flag

    def __init__(self, number, text):
        '''Метод инициализации объекта.'''

        self.number = number
        self.text = text

    def __str__(self):
        '''Метод строчного вывода.'''

        return f'{"".join(x for x in self.archText)} - архив, текущий номер {self.number}'

    def __repr__(self):
        '''Метод вывода архива.'''

        return f'{self.text}'

    def docs(self):
        '''Метод вывода информации документации класса.'''
        return self.__doc__

t = Archive(12, "jksagdjsagdkjalhsdk aksjdhlka jahdk kjahs")
t2 = Archive(12, "jksagdjsagdkjalhsdk sadqqqqq qqqq")
print()
print(t2)
print(repr(t2))

help(t)
help(Archive)