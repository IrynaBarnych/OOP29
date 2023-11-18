# Завдання 3
# Створіть базовий клас «Тварина» та похідні класи:
# «Тигр», «Крокодил», «Кенгуру». Встановіть за допомогою конструктора ім’я кожної тварини та її характеристики.
# Створіть для кожного класу необхідні методи та поля.
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.sound = sound
        self.species = species

    def make_sound(self):
        print(f'{self.species} {self.name} каже {self.sound}')
    def move(self):
        print(f'{self.species} {self.name} пригає')
    def swim(self):
        print(f"{self.species} {self.name} плаває")

class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, "Tiger", "Roar")

    def swim(self):
        super().swim()

class Crocodie(Animal):
    def __init__(self, name):
        super().__init__(name, "Crocodie", "Rrrrrrrr")

    def swim(self):
        super().swim()

class Kangaroo(Animal):
    def __init__(self, name):
        super().__init__(name, "Kangaroo", "snore")

    def move(self):
        super().move()

tiger = Tiger("Шерхан")
crocodie = Crocodie("Локі")
kangaroo = Kangaroo("Ді")
tiger.make_sound()
crocodie.make_sound()
kangaroo.make_sound()
crocodie.swim()
tiger.swim()
kangaroo.move()





