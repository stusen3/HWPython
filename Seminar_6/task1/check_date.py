import time


def ch_date(input_date):
    input_year = int(input_date[-4:])
    try:
        time.strptime(input_date, '%d.%m.%Y')
        __check_year(input_year)
        return True
    except ValueError:
        return False

def __check_year(year):
    if (year % 4 == 0) \
        and (year % 100 != 0) \
        or (year % 400 == 0):
        print("Данный год является високостный")
    else:
        print("Данный год не является високостным")

if __name__ == '__main__':
    print(ch_date(input('Введите дату формата DD.MM.YYYY:  ' + '\n' + '>>>>> ')))


########################### или с использованием класса  #############################
#import time

#class Check_Date:
#    def ch_date(self, input_date):
#       input_year = int(input_date[-4:])
#        try:
#            time.strptime(input_date, '%d.%m.%Y')
#            self.__check_year(input_year)
#            return True
#        except ValueError:
#            return False

#    def __check_year(self, year):
#        if (year % 4 == 0) \
#                and (year % 100 != 0) \
#                or (year % 400 == 0):
#            print("Данный год является високостный")
#        else:
#            print("Данный год не является високостным")

#if __name__ == '__main__':
#    print(Check_Date().ch_date(input('Введите дату формата DD.MM.YYYY:  ' + '\n' + '>>>>> ')))