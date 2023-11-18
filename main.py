# Завдання 1
# Створіть клас Human, який міститиме інформацію про людину.
# За допомогою механізму успадкування реалізуйте клас Builder (містить інформацію про будівельника),
# клас Sailor (містить інформацію про моряка), клас Pilot (містить інформацію про льотчика).
# Кожен із класів має містити необхідні для роботи методи.


class Human:
    def __init__(self, name, date_of_birth, registration, citizenship):
        self.name = name
        self.date_of_birth = date_of_birth
        self.registration = registration
        self.citizenship = citizenship

    def display_info(self):
        print(f'Ім\'я: {self.name}')
        print(f'Дата народження: {self.date_of_birth}')
        print(f'Громадянство: {self.citizenship}')
        print(f'Реєстрація: {self.registration}')

class Builder(Human):
    def __init__(self, name, date_of_birth, registration, citizenship, certificate, experience, qualification):
        super().__init__(name, date_of_birth, registration, citizenship)
        self.certificate = certificate
        self.experience = experience
        self.qualification = qualification

    def display_info(self):
        super().display_info()
        print(f'Інформація про сертифікат: {self.certificate}')
        print(f'Інформація про досвід роботи: {self.experience}')
        print(f'Інформація про кваліфікацію: {self.qualification}')

    def new_experience(self):
        print(f"{self.name} ")

    def new_qualification(self):
        print(f"{self.name} ")


class Sailor(Human):
    def __init__(self, name, date_of_birth, registration, citizenship, rank, experience_at_sea):
        super().__init__(name, date_of_birth, registration, citizenship)
        self.rank = rank
        self.experience_at_sea = experience_at_sea

    def display_info(self):
        super().display_info()
        print(f'Інформація про досвід на морі: {self.experience_at_sea}')
        print(f'Інформація про ранг: {self.rank}')


class Pilot(Human):
    def __init__(self, name, date_of_birth, registration, citizenship, license_type, flying_experience):
        super().__init__(name, date_of_birth, registration, citizenship)
        self.license_type = license_type
        self.flying_experience = flying_experience

    def display_info(self):
        super().display_info()
        print(f'Інформація про тип ліцензії: {self.license_type}')
        print(f'Інформація про досвід польоту: {self.flying_experience}')


# Приклад використання:

builder_info = Builder("Петро", "01.01.1990", "м. Київ", "Україна",
                       "Будівельний сертифікат", "10 років", "Вища")

sailor_info = Sailor("Олександр", "15.05.1985", "м. Одеса", "Україна",
                     "Капітан", "20")

pilot_info = Pilot("Іван", "03.12.1978", "м. Київ", "Україна",
                   "Комерційна", "5000")

print("Інформація про будівельника:")
builder_info.display_info()

print("\nІнформація про моряка:")
sailor_info.display_info()

print("\nІнформація про пілота:")
pilot_info.display_info()









