class Animal:
    def __init__(self, name,species, sound):
        self.name = name
        self.sound = sound
        self.species = species

    def make_sound(self):
        print(f'{self.name} каже {self.sound}')
    def move(self):
        print(f'{self.species} {self.name} рухатися')
    def move(self):
        print(f'{self.species} {self.name} плаває')

class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, "Tiger", "Road")

    def swim(self):
        super().swim()


class Crocodile(Animal):
    def __init__(self, name):
        super().__init__(name, "Crocodale", "Rrrr")

    def swim(self):
        super().swim()

tiger =Tiger ("Loki")
crocodie = Crocodile("Sherhan")
crocodie.swim()
tiger.swim()




