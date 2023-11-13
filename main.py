#успадкування
class Animal:
    def sound(self):
        print("гучно оре")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("гавкає")
dog = Dog()
dog.sound()