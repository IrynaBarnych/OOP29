# Завдання 3
# Запрограмуйте клас Money (об’єкт класу оперує однією валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої
# частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
# зменшення ціни на задане число. Для кожного з класів реалізуйте необхідні методи та поля.

class Money:
    def __init__(self, currency, whole_units, fractional_units):
        self.currency = currency
        self.whole_units = whole_units
        self.fractional_units = fractional_units

    def display_amount(self):
        print(f'{self.whole_units} {self.currency} {self.fractional_units} копійок')

    def set_amount(self, whole_units, fractional_units):
        self.whole_units = whole_units
        self.fractional_units = fractional_units

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        super().__init__()

    def decrease_price(self, amount):
        self.price.whole_units -= amount.whole_units
        self.price.fractional_units -= amount.fractional_units

    def display_product_info(self):
        print(f'Продукт: {self.name}')
        print('Ціна:')
        self.price.display_amount()

money1 = Money("UAH", 750000000, 55)


product1 = Product("Танк", money1)
product1.display_product_info()


discount = Money("UAH", 10500, 0)
product1.decrease_price(discount)


product1.display_product_info()






