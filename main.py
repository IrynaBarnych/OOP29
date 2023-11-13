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

class Parent:
    def __init__(self, name):
        self.name = name
        print("Корисна річ")
class Clild(Parent):
    def __init__(self, name, additional_info):
        #self.name = name
        super().__init__(name) #виклик конструктора батьківського класу
        self.additional_info = additional_info
child = Clild("Oleg", "information")
print(child.name, child.additional_info)
