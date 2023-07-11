# Напишите ФУНКЦИЮ ГРУППОВОГО ПЕРЕИМЕНОВАНИЯ ФАЙЛОВ. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов 
# ✔ принимать параметр "количество цифр в порядковом номере" 
# ✔ принимать параметр "расширение исходного файла" 
# ✔ принимать параметр "расширение конечного файла" 
# ✔ принимать диапазон сохраняемого оригинального имени (т.е. первоначального имени файла)
# Переименование должно работать только для этих файлов внутри каталога
# При переименовании в конце имени добавляется порядковый номер 

##### Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
##### К ним прибавляется желаемое конечное имя, если оно передано. 
##### Далее счётчик файлов и расширение.

import os


def renam_files(new_name: str, numbers: int = 1, one_expansion: str = '',
            end_expansion: str = '', range_original_name: list = []):
    
    # создание списка файлов в текущей дериктории
    files_directory = os.listdir()  
    if len(str(len(files_directory))) > numbers:
        numbers = len(str(len(files_directory)))


    START = 1

    # генератор символов '0' в строке наименования файла
    file_number = ''
    while numbers:
        file_number += '0'
        numbers -= 1
    
    # проверка файлов в текущей директории
    for file in files_directory:
        if file == "task7.py":   
            continue
        if len(file.split('.')) <= 1:  
            continue
        
        count_origin_name, expansion_origin_file = '', file.split('.')[1]
        
        if one_expansion != '' and expansion_origin_file != one_expansion:
            continue
        if end_expansion == '':
            end_expansion = expansion_origin_file
                    
        file_number = file_number[:-len(str(START))] + str(START)
                
        if len(range_original_name) == 2:
            count_origin_name = file[range_original_name[0] - 1:range_original_name[1]:]
        
        os.rename(file, f'{count_origin_name}{new_name}{file_number}.{end_expansion}')

        START += 1


renam_files('_file_', 2, 'csv', 'txt', [3, 6])
