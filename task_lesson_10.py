# Задача 1

# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def len(self):
#         return 2 * 3.14 * self.r
#
#     def sq(self):
#         return 3.14 * self.r ** 2
#
#
# crc = Circle(5)
# print(crc.len())
# print(crc.sq())

# Задача 2

# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

# class Rectangle:
#     def __init__(self, a, b=None):
#         if b == None:
#             b = a
#         self.a = a
#         self.b = b
#
#     def perimeter(self):
#         return (self.a + self.b) * 2
#
#     def sq(self):
#         return self.a * self.b
#
#
# rec = Rectangle(5)
# print(rec.a)
# print(rec.b)
# print(rec.perimeter())
# print(rec.sq())

# Задача 3

# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.

# class Persona:
#
#     def __init__(self, f_name: str, l_name: str, age: int):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.__age = age
#
#     def __birthday(self):
#         self.__age += 1
#
#     def get_age(self):
#         return self.__age
#
#     def full_name(self):
#         return self.f_name + " " + self.l_name
#
#
# person1 = Persona("Ivan", "Ivanov", 59)
# print(f'Возраст = {person1.get_age()}')
# print(person1.full_name())

# Задача 4

# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер,
# уровень доступа, вычисляемый как остаток от деления суммы цифр id на семь.

# class Employer(Persona):
#     def __init__(self, f_name: str, l_name: str, age: int, id: int):
#         self.id = id
#         super().__init__(f_name, l_name, age)
#
#     def level(self):
#         return sum(int(num) for num in str(self.id)) % 7
#
#
# empl = Employer("Lilia", " Sorokina", 30, 512647)
# print(f'Возраст = {empl.get_age()}')
# print(empl.full_name())
# print(empl.level())

# Задача 5

# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п..
# У каждого класса должны быть как общие свойства, например имя,
# так и специфичные для класса.
# Для каждого класса создайте метод,
# выводящий информацию специфичную для данного класса.

# Задача 6

# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс 'Животное'.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

# Задача 5 и задача 6 вместе.

# Вариант 1

# import random
#
# class Animals:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def _birthday(self):
#         self.age += 1
#
#
# class Fish(Animals):
#     def __init__(self, name: str, age: int, areal: str):
#         self.areal = areal
#         super().__init__(name, age)
#
#     def say(self):
#         print("буль-буль")
#
#     def eat(self):
#         print("ням-ням")
#
#     def child(self):
#         a = list(self.name)
#         random.shuffle(a)
#         a = "".join(a)
#         return Fish(a, 0, self.areal)
#
#
# class Birds(Animals):
#     def __init__(self, name: str, age: int, size_wings: int):
#         self.size_wings = size_wings
#         super().__init__(name, age)
#
#     def wings(self):
#         if self.size_wings > 100:
#             print("Это большая птица")
#         else:
#             print("Это маленькая птичка")
#
#     def say(self):
#         print("чик-чирик")
#
#     def eat(self):
#         print("ням-ням")
#
#
# fish1 = Fish("karl", 2, "ocean")
# fish1.say()
# fish1.eat()
# print(fish1.get_age())
# print(fish1.get_name())
# fish2 = fish1.child()
# fish2.say()
# fish2.eat()
# print(fish2.get_age())
# print(fish2.get_name())
# bird1 = Birds("Chig", 2, 105)
# bird1.wings()
# bird1.say()
# print(bird1.name)

# Задача Алексея

# class MyList():
#
#     def __init__(self, spisok):
#         self.spisok = spisok
#
#     def getList(self):
#         return self.spisok
#
#     def sortSpisok(self):
#         return sorted(self.spisok)
#
#     def sumA_B(self, obj):
#         obj2 = self.spisok.copy()
#         obj2.extend(obj.getList())
#         #print('!!!!!!!', obj2)
#         f = MyList(obj2)
#         return f
#
#     def __add__(self, other):
#         return self.sumA_B(other)
#
#     def __str__(self):
#         return "".join(str(num) for num in self.spisok)
#
#
# obj1 = MyList([1,45,0,3,5,2])
# print(obj1.sortSpisok())
# obj2 = MyList([0,0,0])
# f = obj1.sumA_B(obj2)
# print(f.getList())
# #print(obj1.s)
# print(obj1.getList())
# b = obj1+obj2
# print('ffff', b)