class ValidDataError(Exception):
    '''Класс исключения к задаче ПРЯМОУГОЛЬНИКИ
    (сложение, вычитание прямоугольников, нахождение периметра и площади)'''

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 and self.b <= 0:
            return f"Ошибка ввода: обе стороны имеют невалидные значения = {self.a}; {self.b}"
        else:
            if self.a <= 0:
                return f"Ошибка ввода: сторона имеет невалидное  значение = {self.a} "
            else:
                return f"Ошибка ввода: сторона имеет невалидное  значение  = {self.b}"


class SizeError(Exception):
    '''Класс исключения к задаче с МАТРИЦАМИ 
    (сравнение, сложение и перемножение матриц)'''

    def __init__(self, action: str):
        self.action = action

    def __str__(self):
        if self.action == '+':
            return f"Ошибка! Сложить матрицы нельзя, они разных размеров"
        elif self.action == '*':
            return f"Ошибка! Перемножить матрицы нельзя, они не соответствуют размерности"
        else:
            return f"Ошибка! Сравнить матрицы нельзя, они разных размеров"

class ValidIntError(Exception):
    '''Класс исключения к игре УГАДАЙКА'''

    def __str__(self):
        return 'Ошибка! Введенные данные не являются целым числом.'