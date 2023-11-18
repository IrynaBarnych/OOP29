# Завдання 2
# Створіть клас Passport (паспорт), який міститиме паспортну інформацію про громадянина заданої країни.
# За допомогою механізму успадкування реалізуйте клас ForeignPassport (закордонний паспорт), похідний
# від Passport.
# Нагадаємо, що закордонний паспорт містить, крім паспортних даних, дані про візи і номер закордонного
# паспорта. Кожен із класів має містити необхідні методи.


class Passport:
    def __init__(self, name, date_of_birth, citizenship, registration):
        self.name = name
        self.date_of_birth = date_of_birth
        self.citizenship = citizenship
        self.registration = registration

    def display_info(self):
        print(f'Ім\'я: {self.name}')
        print(f'Дата народження: {self.date_of_birth}')
        print(f'Громадянство: {self.citizenship}')
        print(f'Реєстрація: {self.registration}')


class ForeignPassport(Passport):
    def __init__(self, name, date_of_birth, citizenship, registration, data_on_visas, number_foreign_passport):
        super().__init__(name, date_of_birth, citizenship, registration)
        self.data_on_visas = data_on_visas
        self.number_foreign_passport = number_foreign_passport

    def display_info(self):
        super().display_info()
        print(f'Інформація про візи: {self.data_on_visas}')
        print(f'Номер закордонного паспорта: {self.number_foreign_passport}')






