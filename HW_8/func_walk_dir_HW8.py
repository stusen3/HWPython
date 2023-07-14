#  ПРОХОД ПО ПАПКАМ
#  Результаты обхода сохранить в файлы json, csv и pickle. 


import os
import csv
import json
import pickle

FR = os.getcwd()     
MB = 1024**2

def walk_dir(start_folder):
    head_list = ('Имя файла', 'Директория', 'Tип', 'Размер')
    global_list_obj = []
    for address, dirs, files in os.walk(start_folder):
        for file in files:
            global_list_obj.append({head_list[0] : file,
                                    head_list[1] : os.path.basename(address),
                                    head_list[2] : 'file',
                                    head_list[3] : os.path.getsize(os.path.join(address, file))/MB
                                    })
        for th_dir in dirs:
            size_th_dir = size_dir(os.path.join(address, th_dir))
            global_list_obj.append({head_list[0] : th_dir,
                                    head_list[1] : os.path.basename(address),
                                    head_list[2] : 'directory',
                                    head_list[3] : size_th_dir/MB})
    json_write(global_list_obj)
    csv_write(global_list_obj, head_list)
    pickle_write(global_list_obj)


def size_dir(folder):
    sum_size = 0
    lst_dir = os.listdir(folder)
    for el in lst_dir:
        path_file = os.path.join(folder, el)
        if os.path.isdir(path_file):
            sum_size += size_dir(path_file)
        if os.path.isfile(path_file):
            sum_size += os.path.getsize(path_file)
    return sum_size

def json_write(data, f_name = 'lst_files.json'):
    with open(f_name, 'w') as file:
        json.dump(data, file)
    print('Сохранение json файла завершено')

def csv_write(data, list_heads, f_name = 'lst_files.csv'):
    with open(f_name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list_heads)
        writer.writeheader()
        writer.writerows(data)
    print('Сохранение csv файла завершено')

def pickle_write(data, f_name = 'lst_files.pickle'):
    with open(f_name, 'wb') as file:
        pickle.dump(data, file)
    print('Сохранение pickle файла завершено')

if __name__ == '__main__':
    walk_dir(FR)