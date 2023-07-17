# Собрать пакет с играми 


from seminar_task9 import ugaday_function
from bankomat import search_Index, choice_Method


if __name__ == '__main__':
    game = ugaday_function(5, 3)
    print(game())

    id_client = int(input('Укажите свой ID: '))
    index = search_Index(id_client)
    choice_Method(index)