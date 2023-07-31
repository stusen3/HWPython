# Задача УГАДАЙ ЧИСЛО
from random import randint
from My_Exception import ValidIntError


MAX_COUNT = 5

print()
print('Число загадано от 1 до 10! Даю 5 попыток чтобы угадать')
rnd_num = randint(1, 10)
count = 0
while count < MAX_COUNT:
    print('Попыток осталось:', MAX_COUNT-count)
    box = input('Введи свой варинт числа: ')
    print()
    if box.isdigit():
        user_num = int(box)
    else:
        raise ValidIntError()
    match user_num:
        case user_num if user_num == rnd_num:
            count += 1
            print('Число угадано! Ты использовал: ', count, ' попыток')
            break
        case user_num if user_num > rnd_num:
            count += 1
            print()
            print('Загаданое число меньше')
        case user_num if user_num < rnd_num:
            count += 1
            print('Загаданое число больше')
else:
    print('Проиграно! Число не угадано! Все попытки использованы!')