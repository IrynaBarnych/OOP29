# Завдання 1
# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас Coffee Machine (містить інформацію про кавомашину),
# клас Blender (містить інформацію про блендер), клас MeatGrinder (містить інформацію про м’ясорубку).
# Кожен із класів має містити необхідні для роботи методи.

class Device:
    def __init__(self, name, power, application, weight):
        self.name = name
        self.power = power
        self.application = application
        self.weight = weight

    def display_info(self):
        print(f'Назва: {self.name}')
        print(f'Потужність, кВт: {self.power}')
        print(f'Застосування: {self.application}')
        print(f'Вага, кг: {self.weight}')


class Coffee_Machine(Device):
    def __init__(self, name, power, application, weight, typ_coffee, milk):
        super().__init__(name, power, application, weight)
        self.typ_coffee = typ_coffee
        self.milk = milk

    def display_info(self):
        super().display_info()
        print(f'Інформація про тип кави: {self.typ_coffee}')
        print(f'Інформація про використання молока: {self.milk}')


class Blender(Device):
    def __init__(self, name, power, application, weight, number_of_nozzles, mixer):
        super().__init__(name, power, application, weight)
        self.number_of_nozzles = number_of_nozzles
        self.mixer = mixer

    def display_info(self):
        super().display_info()
        print(f'Інформація про кількість насадок, шт.: {self.number_of_nozzles}')
        print(f'Чи можна використовувати як міксер: {self.mixer}')


class MeatGrinder(Device):
    def __init__(self, name, power, application, weight, electric_or_manual):
        super().__init__(name, power, application, weight)
        self.electric_or_manual = electric_or_manual

    def display_info(self):
        super().display_info()
        print(f"М'ясоручка ручна або електрична: {self.electric_or_manual}")

# Приклад використання:

coffee_machine_info = Coffee_Machine("кавомашина", 1200, "приготування кави",
                                     10, "еспресо", "так")
blender_info = Blender("Блендер", 500, "змішування продуктів",
                       5, 3, "так")
meatGrinder_info = MeatGrinder("м'ясорубка", 800, "приготування м'ясних страв",
                               7, "електрична")

print("Інформація про кавомашину:")
coffee_machine_info.display_info()

print("\nІнформація про блендер:")
blender_info.display_info()

print("\nІнформація про м'ясорубку:")
meatGrinder_info.display_info()





