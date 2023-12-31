# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

import check_date

if __name__ == '__main__':
    print('Введите дату формата DD.MM.YYYY')
    input_date = input('>>>>> ')
    func_date = check_date
    print(func_date.ch_date(input_date))

########################### или с использованием класса  #############################

import check_date

if __name__ == '__main__':
    print('Введите дату формата DD.MM.YYYY')
    input_date = input('>>>>> ')
    func_date = check_date.Check_Date()
    print(func_date.ch_date(input_date))