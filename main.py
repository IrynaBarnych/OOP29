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

#система школа
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id
    def get_student_id(self):
        return self.student_id
    def display_subject(self, subjects):
        print(f"студент вивчив {self.name} предмети: ")
        for subject in subjects:
            print(subject)
class Teacher(Person):
    def __init__(self, name, age, gender, employee_id):
        super().__init__(self, name, age, gender)
        self.employee_id = employee_id
student1 = Student("Oleg", 15, "male", 12)
student2 = Student("Olga", 16, "female", 13)
print(f"Студент на ім'я {student1.name} з id: {student1.get_student_id}")
student1.display_subject(['Math', 'Scien', 'History'])
