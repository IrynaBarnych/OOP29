#успадкування
class Animal:
    def sound(self):
        print("гучно оре")
class Dog(Animal):
    pass
dog = Dog()
dog.sound()