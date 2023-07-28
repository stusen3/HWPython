# СОЗДАТЬ КЛАСС СТУДЕНТА
import csv
from functools import reduce
from pathlib import Path


class Сheck_name:  
    ''' В классе имеются методы, которые проверяют в ФИО:
         	- наличие первой заглавной буквы,
        	- наличие только букв '''                                

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha():
            raise TypeError(f'Ошибка! "{value}" должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Ошибка! "{value}" должно начинаться с заглавной буквы')


class Student:
    '''  Класс Студент, который имеет методы:
         - считывания с файла список предметов в словарь lessons
         - сохранения новой оценки 
         - подсчета средней оценки  
         - подсчета и сообщения о результате среднего бала по тестам всех предметов  '''

    name = Сheck_name()
    second_name = Сheck_name()
    surname = Сheck_name()
    _jurnal = None

    def __init__(self, name: str, second_name: str, surname: str, jurnal_file: Path):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.jurnal = jurnal_file

    @property
    def jurnal(self):
        return self._jurnal

    @jurnal.setter
    def jurnal(self, jurnal_file: Path):  
  
        self._jurnal = {"jurnal": {}}
        with open(jurnal_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self._jurnal["jurnal"][row[0]] = {"assessments": [], "results_test": [], "average_test": None}
        self._jurnal["middle_assessment"] = None
        self._jurnal["middle_test"] = None

    def __call__(self, lesson: str, number: int, type_est: str = "jurnal"):     
    
        if lesson not in self.jurnal["jurnal"].keys():
            raise AttributeError("Такой предмет отсутствует")
        if type_est == "jurnal":
            if number < 2 or number > 5:
                raise ValueError("Оценка должна быть от 2 до 5")
            self.jurnal["jurnal"][lesson]["assessments"].append(number)
            self.jurnal["middle_assessment"] = self.calculate_average(self.jurnal)
        elif type_est == "тест":
            if number < 0 or number > 100:
                raise ValueError("Оценка должна быть от 0 до 100")
            self.jurnal["jurnal"][lesson]["results_test"].append(number)
                                                               
            self.jurnal["jurnal"][lesson]["average_test"] = reduce(lambda x, y: x + y,\
                            self.jurnal["jurnal"][lesson]\
                                ["results_test"]) / len(self.jurnal["jurnal"]\
                                                        [lesson]["results_test"])
            self.jurnal['middle_test'] = self.calculate_test(self.jurnal)

    @staticmethod
    def calculate_average(jurnal: dict):                    

        all_mark = []
        [all_mark.extend(jurnal["jurnal"][name]["assessments"]) for name in jurnal["jurnal"]]

        return reduce(lambda x, y: x + y, all_mark) / len(all_mark)

    @staticmethod
    def calculate_test(jurnal: dict):                        

        all_mark = []
        [all_mark.extend(jurnal["jurnal"][name]["results_test"]) for name in jurnal["jurnal"]]

        return reduce(lambda x, y: x + y, all_mark) / len(all_mark)

    def __repr__(self):
        result = f'Студент - {self.name} {self.second_name} {self.surname}\nСредняя оценка - {self.jurnal["middle_assessment"]}\nСредний бал по тестам - {self.jurnal["middle_test"]}\n'
        
        result += "\nОценки по предметам:\n"

        for key, value in self.jurnal["jurnal"].items():
            result += f'{key} - {value["assessments"]}\n'
        result += "\nРезультаты по тестам:\n"
        for key, value in self.jurnal["jurnal"].items():
            result += f'{key} - {value["results_test"]}, средний бал - {value["average_test"]}\n'

        return result


if __name__ == '__main__':
    print(f'--' * 30)
    print()
    s1 = Student("Понамарева", "Марина", "Валентиновна", Path('jurnal.csv'))
    s1("математика", 5)
    s1("математика", 86, "тест")
    s1("физика", 5)
    s1("физика", 98, "тест")
    s1("физкультура", 94, "тест")
    s1("физкультура", 5)
    print(s1)
    print(f'--' * 30)

    s2 = Student("Черанёв", "Ян", "витальевич", Path('jurnal.csv'))
    s2("физика", 3)
    s2("физика", 48, "тест")
    s2("математика", 5)
    s2("математика", 80, "тест")
    s2("физкультура", 5)
    s2("физкультура", 100, "тест")
    print(s2)