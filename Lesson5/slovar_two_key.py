# СЛОВАРЬ С ДВУМЯ КЛЮЧАМИ

# Пользователь вводит строку из четырёх 
# или более целых чисел, разделённых символом “/”. 

# Сформируйте словарь, где:
# второе и третье число являются ключами.
# первое число является значением для первого ключа.
# четвертое и все возможные последующие числа 
# хранятся в кортеже как значения второго ключа.


one, two, three, *other = input('Какой текст преобразовать? ').split('/')

################ 2 вариант #####################
# list_value_and_key = input('Введите значения, используя "/" для разделения').split('/')
# list_value_and_key = list(filter(None, list_value_and_key))
# list_value_and_key = [int(item) for item in list_value_and_key]
#
# list_key = [list_value_and_key[i] for i in range(1, 3)]
# list_value = [list_value_and_key[0],
#               tuple(list_value_and_key[i] for i in range(3, len(list_value_and_key)))]
#
# list_dict = dict(zip(list_key, list_value))
# print(list_dict)

#####################  3 вариант ###########################
# list_value_and_key = [int(item) for item in
#                       list(filter(None, input('Введите значения, '
#                                               'используя "/" для разделения ').split('/')))]
#
# print(dict(zip([list_value_and_key[i] for i in range(1, 3)],
#                      [list_value_and_key[0],
#                       tuple(list_value_and_key[i] for i in range(3, len(list_value_and_key)))])))