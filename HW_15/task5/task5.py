# Задача 5

# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае, берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# * Научите функцию распознавать не только текстовое название дня недели и месяца, но и числовые,
# т.е не мая, а 5.

from task4 import text_to_date
import argparse
from datetime import datetime

if __name__ == '__main__':
    months = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн', 7: 'июл', 8: 'авг', 9: 'сен', 10: 'окт',
              11: 'ноя', 12: 'дек'}
    weekdays = {1: 'вт', 2: 'ср', 3: 'чт', 4: 'пт', 5: 'сб', 6: 'вс', 7: 'пн'}

    parser = argparse.ArgumentParser(description="Получаем строку с датой")
    parser.add_argument('-count', type=str, default='1')
    parser.add_argument('-weekday', type=str, default='понeдельник')
    parser.add_argument('-month', type=str, default=months[datetime.now().month])

    args = parser.parse_args()

    weekday = weekdays[int(args.weekday)] if args.weekday.isdigit() and int(args.weekday) in weekdays else args.weekday   
    month = months[int(args.month)] if args.month.isdigit() and int(args.month) in months else args.month  

    print(f'{args.count} {weekday} {month}: ', text_to_date(f'{args.count} {weekday} {month}'))


'''
Запуск в терминале:
python task5.py -count='3-я' -weekday='среда'
python task5.py -count='3-я' -weekday=3
python task5.py -count='3-я' -weekday=3 - month=3
'''