# Задача с матрицами

from My_Exception import SizeError

class Matrix:
    '''
    >>> Matrix([[1, 2, 3],[3, 6, 7],[7, 8, 2],[10, 5, 4]]) == Matrix([[1, 2, 3],[3, 6, 7],[7, 8, 2],[10, 5, 4]])
    True
    >>> Matrix([[1, 2, 4],[5, 6,  8],[2, 5, -2],[10, 5, 0]]) + Matrix([[1, 2, 4],[5, 6,  8], [5, 6,  8], [-2, 2, 0]])
    [2, 4, 8][10, 12, 16][7, 11, 6][8, 7, 0]
    >>> Matrix([[1, 2, 3],[3, 6, 7],[7, 8, 2],[10, 5, 4]]) * Matrix([[2, 8, 3, 5],[6, 4, 1, 0],[7, 3, 1, 9]])
    [35, 25, 8, 32][91, 69, 22, 78][76, 94, 31, 53][78, 112, 39, 86]
    '''

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise SizeError
        else:
            return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])

    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            raise SizeError
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise SizeError
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            return True


    def __repr__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i])
        return s


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)