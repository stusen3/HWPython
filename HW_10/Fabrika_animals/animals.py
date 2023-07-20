# Создать классы  (родительский и несколько дочерних) на тему "Животные".

# Класс животные
class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return (f'{"Class:":8}{type(self).__name__}'
                f'\n{"Name:":8}{self.name}'
                f'\n{"Age:":8}{self.age} months')


# Класс Млекопитающие
class Mammal(Animal):

    def __init__(self, name: str, age: int, wool: str, color: str, voice: str):
        super().__init__(name, age)
        self.wool = wool
        self.color = color
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Wool:":8}{self.wool}'
                f'\n{"Color:":8}{self.color}'
                f'\n{"Voice:":8}{self.voice}\n')


# Класс Птицы
class Bird(Animal):

    def __init__(self, name: str, age: int, color: str, voice: str):
        super().__init__(name, age)
        self.color = color
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}'
                f'\n{"Voice:":8}{self.voice}\n')


# Класс Рыбы
class Fish(Animal):

    def __init__(self, name: str, age: int, color: str, voice: str):
        super().__init__(name, age)
        self.color = color
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}\n'
                f'\n{"Voice:":8}{self.voice}\n')


if __name__ == '__main__':
    mammal = Mammal('Немецкая овчарка', 3, "длинношёрстная", "черная", "гав-гав")
    print(f'{mammal.name = }, {mammal.age = }, {mammal.wool = }, {mammal.color = }, {mammal.voice = }, {mammal.get_info()}')

    bird = Bird('Фламинго', 10, "розовый", "писк-писк")
    print(f'{bird.name = }, {bird.age = }, {bird.color = }, {bird.voice = }, {bird.get_info()}')

    fish = Fish('Скумбрия', 6, "тёмно-синяя", "буль-буль")
    print(f'{fish.name = }, {fish.age = }, {fish.color = }, {fish.voice = }, {fish.get_info()}')