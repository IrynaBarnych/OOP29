class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.sound = sound
        self.species = species

    def make_sound(self):
        print(f'{self.species} {self.name} каже {self.sound}')
    def move(self):
        print(f'{self.species} {self.name} рухатися')
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

tiger = Tiger("Шерхан")
crocodie = Crocodie("Локі")
crocodie.swim()
tiger.swim()
crocodie.make_sound()




