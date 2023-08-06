import argparse
from Matrix import Matrix
from Convert import convert_format

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Получаем операцию над двумя матрицами")
    parser.add_argument('-m_1', type=list, action='append', default=[['1', '1', '1', ' ', '1', '1', '1',' ', '1', '1', '1', ' ', '1', '1', '1']])
    parser.add_argument('-m_2', type=list, action='append', default=[['1', '1', '1', ' ', '1', '1', '1',' ', '1', '1', '1', ' ', '1', '1', '1']])
    parser.add_argument('-operation', type=str, default='+')

    args = parser.parse_args()

    m_1 = convert_format(args.m_1)
    m_2 = convert_format(args.m_2)

    if args.operation == '+':
        print(f'сложение: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) + Matrix(m_2)} '))
    elif  args.operation == '*':
        print(f'умножение: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) * Matrix(m_2)} '))
    elif args.operation == '=':
        print(f'сравнение: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) == Matrix(m_2)} '))
    else:
        print(f'Операция {args.operation} над матрицами не предусмотрена')

'''
Запуск в терминале:
# python HW15/Matrix_terminal.py
# python HW15/Matrix_terminal.py -m_1='124 252 253' -m_2='124 252 253'
# python HW15/Matrix_terminal.py -m_1='124 252 253' -m_2='124 252 253' -operation='='
# python HW15/Matrix_terminal.py -m_1='124 252 253' -m_2='124 252 253' -operation='*'
'''