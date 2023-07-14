#  ВЫВОД ПИКЛ СТРОКИ ИЗ csv ФАЙЛА

import csv, pickle

def reader_csv(f_name):
    with open(f_name, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(pickle.dumps(row))

if __name__ == '__main__':
    reader_csv('new_csv.csv')