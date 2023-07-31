# Задача с прямоугольниками

from My_Exception import ValidDataError


class Rectangle:

    def __init__(self, side_a: float, side_b: float | None =None):
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)

    def get_square(self):
        return self._side_a * self._side_b

    def __add__(self, other):
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __str__(self):
        return f"Получили прямоугольник со сторонами - {self._side_a} и {self._side_b}; периметром - {self.get_perimeter()}; площадью - {self.get_square()}"

def main():
    box = False
    while True:
        if box:
            choise = input("1 - Выйти\n2 - Продолжить\n")
            if choise == '1':
                break
        box = True

        try:
            a_1 = float(input('\nВведите первую сторону первого прямоугольника: '))
            b_1 = float(input('Введите первую сторону второго прямоугольника: '))
            a_2 = float(input('Введите вторую сторону первого прямоугольника: '))
            b_2 = float(input('Введите вторую сторону второго прямоугольника: '))
        except ValidDataError as e:
            print(f"\nФормат ввода не верный => {e}\nВсе стороны прямоугольников по умолчанию равны 1\n")
            a_1 = a_2 = b_1 = b_2 = 1

        if a_1 <= 0 or b_1 <= 0:
            raise ValidDataError(a_1, b_1)
        if a_2 <= 0 or b_2 <= 0:
            raise ValidDataError(a_2, b_2)

        rectangle_1 = Rectangle(a_1, b_1)
        print(f'\nПериметр 1-го прямоугольника = {rectangle_1.get_perimeter()},  площадь 1-го прямоугольника = {rectangle_1.get_square()}')
        rectangle_2 = Rectangle(a_2, b_2)
        print(f'Периметр 2-го прямоугольника = {rectangle_2.get_perimeter()}, площадь 1-го прямоугольника = {rectangle_2.get_square()}')
        choise = input("\nВыберите операцию для прямоугольников:\n1 - сложить\n2 - вычесть\n3 - выйти\n")
        match choise:
            case '1':
                rectangle_3 = rectangle_1 + rectangle_2
                print(rectangle_3)

            case '2':
                rectangle_3 = rectangle_1 - rectangle_2
                print(rectangle_3)
            case _:
                break

if __name__ == '__main__':
    main()