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

    def new_name(self):
        print(f'{self.name} Шевченко Т.Г.')

    def new_date_of_birth(self):
        print(f'{self.name} 09.03.1814')

    def new_citizenship(self):
        print(f"{self.name} українець")

    def new_registration(self):
        print(f"{self.name} селі Моринці, Житомирська область")


class Builder:
    def __init__(self, name, certificate, experience, qualification):
        self.name = name
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









