# Завдання 2
# Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте клас Frigate (містить інформацію про фрегат), клас Destroyer (містить
# інформацію про есмінця), клас Cruiser (містить інформацію про крейсер).
# Кожен із класів має містити необхідні для роботи методи.

class Ship:
    def __init__(self, name, displacement, length, max_speed):
        self.name = name
        self.displacement = displacement
        self.length = length
        self.max_speed = max_speed

    def display_info(self):
        print(f'Назва корабля: {self.name}')
        print(f'Водотоннажність: {self.displacement} тонн')
        print(f'Довжина: {self.length} метрів')
        print(f'Максимальна швидкість: {self.max_speed} вузлів')


class Frigate(Ship):
    def __init__(self, name, displacement, length, max_speed, missile_system):
        super().__init__(name, displacement, length, max_speed)
        self.missile_system = missile_system

    def display_info(self):
        super().display_info()
        print(f'Інформація про систему ракет: {self.missile_system}')


class Destroyer(Ship):
    def __init__(self, name, displacement, length, max_speed, artillery, torpedoes):
        super().__init__(name, displacement, length, max_speed)
        self.artillery = artillery
        self.torpedoes = torpedoes

    def display_info(self):
        super().display_info()
        print(f'Інформація про артилерію: {self.artillery}')
        print(f'Інформація про торпеди: {self.torpedoes}')


class Cruiser(Ship):
    def __init__(self, name, displacement, length, max_speed, num_missiles, radar_system):
        super().__init__(name, displacement, length, max_speed)
        self.num_missiles = num_missiles
        self.radar_system = radar_system

    def display_info(self):
        super().display_info()
        print(f'Кількість ракет на борту: {self.num_missiles}')
        print(f'Інформація про радарну систему: {self.radar_system}')

frigate_info = Frigate("Фрегат", 3500, 123, 30, "Aegis")
destroyer_info = Destroyer("Есмінець", 5000, 150, 35, "120 mm",
                           "torpedoes")
cruiser_info = Cruiser("Крейсер", 8000, 180, 25, 80,
                       "AN/SPY-1D radar")

print("Інформація про фрегат:")
frigate_info.display_info()

print("\nІнформація про есмінець:")
destroyer_info.display_info()

print("\nІнформація про крейсер:")
cruiser_info.display_info()






