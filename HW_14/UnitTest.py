from DocTest import Matrix
import unittest


class TestMatrix(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(str(Matrix([[1, 2, 3], [3, 6, 7], [7, 8, 2]]) + Matrix([[9, 8, 7], [7, 4, 3], [3, 2, 8]])), '[10, 10, 10][10, 10, 10][10, 10, 10]')

    def test_mul(self):
        self.assertEqual(str(Matrix([[1, -2], [25, -5]]) * Matrix([[11, -8], [15, 0]])), '[-19, -8][200, -200]')


if __name__ == '__main__':
    unittest.main(verbosity=2)