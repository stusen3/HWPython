CONST = 1


def convert_positions(user_str):       # Функция преоброзования строки в двумерный словарь
    lst_start = user_str.split()
    lst_finish = []
    for el in lst_start:
        lst_finish.append(list(map(int, el.split(','))))
    return lst_finish


def check_posititions(lst_p):             # Функция проверки пересечения ферзей
    clms, rows = map(list, zip(*lst_p))   # конвертируем наборы значений в 2 списка столбцы и строки
    for el in clms:                       # проверяем дубликаты по столбцам
        if clms.count(el) > CONST:
            return False
    for el in rows:                       # проверяем дубликаты по строкам
        if rows.count(el) > CONST:
            return False
    result_list = []                      # если дубликатов строк нет, конвертировать 2 словаря в один (индекс - столбец, строка - значение)
    for i in range(len(clms)):
        result_list.insert(clms[i]-CONST, rows[i]-CONST)
    for i in range(len(result_list)-CONST):
        for j in range(CONST, len(result_list) - i):
            if result_list[i] + j == result_list[i + j] or result_list[i] - j == result_list[i + j]:
                return False
    return True