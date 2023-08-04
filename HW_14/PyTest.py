import pytest

from My_Exception import SizeError
from DocTest import Matrix


def test_sum():

   assert (str(Matrix([[1, -2], [25, -5]]) + Matrix([[11, -8], [15, 0]]))) == '[12, -10][40, -5]', "Неверная сумма!"


def test_mul():

    assert (str(Matrix([[1, -2], [25, -5]]) * Matrix([[11, -8], [15, 0]]))) == '[-19, -8][200, -200]', "Неверный результат произведения!"


def test_format():

    with pytest.raises(SizeError):
        Matrix([[1, -2], [25, -5]]) + Matrix([[11, -8], [15, 0], [16, 10]])
        Matrix([[1, -2], [25, -5]]) * Matrix([[11, -8], [15, 0], [16, 10]])


if __name__ == '__main__':
    pytest.main(['-v'])