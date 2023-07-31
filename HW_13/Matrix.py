# Задача с матрицами

from My_Exception import SizeError


class Matrix:

    def __init__(self, matrx):
        self._matrx = matrx

    def get_matrix(self):
        return self._matrx

    def __add__(self, other):
        if len(self._matrx) != len(other._matrx) or len(self._matrx[0]) != len(other._matrx[0]):
            raise SizeError("+")
        else:
            return Matrix([[self._matrx[i][j] + other._matrx[i][j] for j in range(len(self._matrx[0]))] for i in range(len(self._matrx))])

    def __mul__(self, other):
        if len(self._matrx[0]) != len(other._matrx):
            raise SizeError("*")
        else:
            new_matrx = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matrx)] for i_row in self._matrx]
            return Matrix(new_matrx)

    def __eq__(self, other):
        if len(self._matrx) != len(other._matrx) or len(self._matrx[0]) != len(other._matrx[0]):
            raise SizeError("eq")
        else:
            for i in range(len(self._matrx)):
                for j in range(len(self._matrx[0])):
                    if self._matrx[i][j] != other._matrx[i][j]:
                        return False
            return True

    def __str__(self):
        s = ''
        for i in range(len(self._matrx)):
            s += str(self._matrx[i]) + '\n'
        return s


if __name__ == '__main__':

    mx_1 = [[1, 2, 3],
          [3, 6, 7],
          [7, 8, 2],
          [10, 5, 4]]

    mx_2 = [[9, 8, 7],
          [7, 4, 3],
          [3, 2, 8],
          [0, 5, 6]]

    m_3 = [[2, 8, 3, 5],
          [6, 4, 1, 0],
          [7, 3, 1, 9]]

    matrx_1 = Matrix(mx_1)
    matrx_2 = Matrix(mx_2)
    matrx_3 = Matrix(m_3)

    print()
    print("Cравнение матриц:")
    print(matrx_1 == matrx_1)
    print(matrx_1 == matrx_2)
    print()

    print("Cложение матриц:")
    matrx_sum = matrx_1 + matrx_2
    print(matrx_sum)

    print("Умножение матриц:")
    print(matrx_1 * matrx_3)