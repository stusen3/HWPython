class SizeError(Exception):
    def __str__(self):
        return f"Ошибка: Матрицы нельзя сравнить, они разных размеров!"