# Решить одну из предыдущей задачи, создав класс (превратить функции в методы класса, 
# а параметры в свойства предыдущей задачи.
# Задача должна решаться через вызов методов экземпляра.
import bankomat_msg


class Atm:
    __START_NUM = 0
    __STEP = 1
    __MAX_CUNT = 3
    __UNRICH_LIMIT = 5_000_000
    __PROCENT_RICH = 0.9
    __MULTYPLICITY = 50
    __BONUS = 1.03
    __TAX = 1.015
    def __init__(self):
        self.__balance = self.__START_NUM
        self.__count_operations = self.__START_NUM
        self.__history_list = []
        print(bankomat_msg.start_msg)

    def get_balance(self):
        return self.__balance

    def rich_tax(self):
        if self.__balance >= self.__UNRICH_LIMIT:
            self.__balance *= self.__PROCENT_RICH

    def __check_cashe(self, ins_sum):
        if ins_sum % self.__MULTYPLICITY == 0:
            return True
        return False

    def __bonus(self):
        if self.__count_operations % self.__MAX_CUNT == self.__START_NUM:
            self.__balance *= self.__BONUS

    def __ap_history(self, msg, inp_sum):
        self.__history_list.append(msg + str(inp_sum))

    def input_money(self, inp_cashe):
        self.rich_tax()
        if self.__check_cashe(inp_cashe):
            self.__balance += inp_cashe
            self.__count_operations += self.__STEP
            self.__bonus()
            self.__ap_history(bankomat_msg.inp_msg, inp_cashe)
            return bankomat_msg.out_balance + str(self.get_balance())
        else:
            return bankomat_msg.cashe_error

    def insert_money(self, ins_cashe):
        self.rich_tax()
        if self.__check_cashe(ins_cashe) and self.__balance > ins_cashe * self.__TAX:
            self.__balance -= ins_cashe * self.__TAX
            self.__count_operations += self.__STEP
            self.__bonus()
            self.__ap_history(bankomat_msg.ins_msg, ins_cashe)
            return bankomat_msg.out_balance + str(self.get_balance())
        else:
            return bankomat_msg.cashe_error

    def history(self):
        self.rich_tax()
        for el in self.__history_list:
            print(el)


atm = Atm()
while(True):
        match input(bankomat_msg.input_ch_msg):
            case '1':
                cashe = int(input(bankomat_msg.input_msg))
                print(atm.input_money(cashe))
            case '2':
                cashe = int(input(bankomat_msg.insert_msg))
                print(atm.insert_money(cashe))
            case '3':
                atm.history()
            case '4':
                print(bankomat_msg.finish_msg)
                break
            case _:
                atm.rich_tax()
                print(bankomat_msg.mistake_msg)