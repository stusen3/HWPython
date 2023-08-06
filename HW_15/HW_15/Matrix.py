# Задача с матрицами

import logging


logging.basicConfig(filename='Log.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class Matrix:

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(f'Сложить мартицы нельзя, их размеры разные:  [{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}] ')

        else:
            new_matr = Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])
            logger.info(f'Сложение:  {self._matr} + {other._matr} = {new_matr}  ')
            return new_matr


    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            logger.error(f'Умножить матрицы нельзя, размеры матриц несовместимы: [{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}]')
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            logger.info(f' Умножение:  {self._matr} * {other._matr} = {new_matr}  ')
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(f'Сравненить матрицы нельзя!')
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            logger.info(f'Сравнение:  {self._matr} = {other._matr} ')
            return True


    def __repr__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i])
        return s


if __name__ == '__main__':

    m_1 = [[1, 2, 3],
          [3, 6, 7],
          [7, 8, 2],
          [10, 5, 4]]

    m_2 = [[9, 8, 7],
          [7, 4, 3],
          [3, 2, 8],
          [0, 5, 6]]

    m_3 = [[2, 8, 3, 5],
          [6, 4, 1, 0],
          [7, 3, 1, 9]]

    print()
    print ("Результат сложения:")
    print(Matrix(m_1) + Matrix(m_2))
    print(Matrix(m_3) + Matrix(m_1))

    print()
    print("Результат сравнения:")
    print(Matrix(m_1) == Matrix(m_1))

    print()
    print("Результат умножения:")
    print(Matrix(m_1) * Matrix(m_3))
    print(Matrix(m_1) * Matrix(m_2))