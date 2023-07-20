# Создайте класс-фабрику.

from animals import Mammal, Bird, Fish

class FabricAnimals:
    def __init__(self, animals: str,  **kwargs):
        self.animals = animals

        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'color':
                self.color = value
            if key == 'voice':
                self.voice = value
            if key == 'wool':
                self.wool = value

    def get_info_animal(self):
        if self.animals == 'Млекопитающее':
            return Mammal(self.name, self.age, self.wool, self.color, self.voice)
        elif self.animals == 'Птица':
            return Bird(self.name, self.age, self.color, self.voice)
        elif self.animals == 'Рыба':
            return Fish(self.name, self.age, self.color, self.voice)


if __name__ == '__main__':
    bird1 = FabricAnimals(animals='Птица', name='Перепелка', age=36, color='серая', voice='чик-чирик').get_info_animal()
    bird2 = FabricAnimals(animals='Птица', name='Попугай', age=6, color='цветной', voice='пр-р-р-ривет').get_info_animal()
    mammal1 = FabricAnimals(animals='Млекопитающее', name='Кошка - шотланская', age=12, wool='длинношёрстная', 
                          color='белый', voice='мяу-мяу').get_info_animal()
    
    print(bird1.get_info())
    print(bird2.get_info())
    print(mammal1.get_info())