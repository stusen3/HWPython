# ФУНКЦИЯ-ГЕНЕРАТОР ДЛЯ ПРОСТЫХ ЧИСЕЛ

# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


#from sympy import *; print([i for i in range(100) if isprime(i)])

#####################  2 вариант  #########################
def is_prime(x):
    for i in range(2, int((x**0.5)+1)):
        if x % i == 0:
            return False
    return True

def gener_integer(x):
    count = 1
    prime_number = 2
    yield prime_number
    while count < x:
        prime_number += 1
        if is_prime(prime_number):
            count += 1
            yield prime_number

print([i for i in gener_integer(100)])