# 📌Добавить к задаче строки документации и методы вывода
#    информации на печать.

# Задачи 5 и 6:
# Задача 5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Задача 6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади.
# Должны работать все шесть операций сравнения.

class Rectangle:
    '''Класс прямоугольник с методами расчета периметра и площади фигуры.'''

    def __init__(self, side_a: int = 1, side_b: int | None = None):
        '''Метод инициализации сторон объекта - прямоугольника.'''
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        '''Метод расчета периметра прямоугольника.'''
        return 2 * (self._side_a + self._side_b)

    def get_area(self):
        '''Метод расчета площади прямоугольника.'''
        return self._side_a * self._side_b

    def __add__(self, other):
        '''Метод сложения двух прямоугольников.'''
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        '''Метод вычетания двух прямоугольников.'''
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __lt__(self, other):
        '''Метод определения поведение оператора сравнения - «<»,
        и возвращает логическое значение.'''
        return self.get_area() < other.get_area()

    def __gt__(self, other):
        '''Метод определяет поведение оператора сравнения «>».
        и возвращает логическое значение.'''
        return self.get_area() > other.get_area()

    def __eq__(self, other):
        '''Метод определяет поведение оператора равенства (==).
        и возвращает логическое значение.'''
        return self.get_area() == other.get_area()

    def __le__(self, other):
        '''Метод определяет поведение оператора «<=».  
        и возвращает логическое значение.'''
        return self.get_area() <= other.get_area()

    def __ge__(self, other):
        '''Метод определяет поведение оператора «>=».
        и возвращает логическое значение.'''
        return self.get_area() >= other.get_area()

    def __ne__(self, other):
        '''Метод определяет поведение оператора «!=».
        и возвращает логическое значение.'''
        return self.get_area() != other.get_area()
    
    def __str__(self):
        '''Метод строчного вывода экземпляра класса Прямоугольник.'''
        return f"Прямоугольник со сторонами: {self._side_a} и {self._side_b} имеет периметр: {self.get_perimeter()}"


if __name__ == '__main__':
    rect1 = Rectangle(3, 5)
    rect2 = Rectangle(2, 3)
    rect3 = rect1 + rect2
    print(rect3)

    rect5 = Rectangle(2, 2)
    rect6 = Rectangle(3, 3)
    print(rect1 < rect2)
    print(rect1 > rect2)
    print(rect1 == rect2)
    print(rect1 <= rect2)
    print(rect1 >= rect2)
    print(rect1 != rect2)

    help(Rectangle)