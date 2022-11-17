# Створити клас Rectangle:
# -він має приймати дві сторони x, y
# -описати поведінку на арифметични методи:
# + сумма площин двох екземплярів ксласу
# - різниця площин двох екземплярів ксласу
# == площин на рівність
# != площин на не рівність
# >, < меньше більше
# при виклику метода len() підраховувати сумму сторін

class Rectangle:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x * self.y + other.x * other.y

    def __sub__(self, other):
        return self.x * self.y - other.x * other.y

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y

    def __ne__(self, other):
        return self.x * self.y != other.x * other.y

    def __lt__(self, other):
        return self.x * self.y < other.x * other.y

    def __gt__(self, other):
        return self.x * self.y > other.x * other.y

    def __len__(self):
        return self.x * 2 + self.y * 2


rec1 = Rectangle(5, 10)
rec2 = Rectangle(10, 20)

print(rec1 + rec2)
print(rec1 - rec2)
print(rec1 == rec2)
print(rec1 != rec2)
print(rec1 < rec2)
print(rec1 > rec2)
print(len(rec1))

###############################################################################
# створити класс Human(name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір ноги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод,
# котрий буде приймати список попелюшок, та шукати ту саму
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1

    def get_count():
        return count

    return inner, get_count


count, get_count = counter()


class Cinderella(Human):
    def __init__(self, name:str, age:int, foot_size: int):
        super().__init__(name, age)
        self.foot_size = foot_size
        count()

    def __str__(self):
        return f'{self.name} - {self.foot_size}'

    def __len__(self):
        return self.age

    @staticmethod
    def get_count():
        print(get_count())


class Prince(Human):
    def __init__(self, name:str, age:int, boot_size: int):
        super().__init__(name, age)
        self.boot_size = boot_size

    def find_cinderella(self, list_of_cinderellas: list[Cinderella]):
        for cin in list_of_cinderellas:
            if cin.foot_size == self.boot_size:
                return cin


prince = Prince('Vasya', 25, 36)

cin1 = Cinderella('Vika', 20, 37)
cin2 = Cinderella('Masha', 22, 38)
cin3 = Cinderella('Katya', 23, 40)
cin4 = Cinderella('Alina', 19, 36)
cin5 = Cinderella('Aliona', 26, 39)

print(prince.find_cinderella([cin1, cin2, cin3, cin4, cin5]))
Cinderella.get_count()

###############################################################################

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є
# класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

from abc import ABC, abstractmethod
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def print(self):
        print(self.name)

    def __init__(self, name:str):
        self.name = name


class Magazine(Printable):
    def print(self):
        print(self.name)

    def __init__(self, name:str):
        self.name = name


class Main:
    printable_list = []

    def add(self, obj: Book | Magazine):
        if isinstance(obj, Book) or isinstance(obj, Magazine):
            self.printable_list.append(obj)

    def show_all_magazines(self):
        for item in self.printable_list:
            if isinstance(item, Magazine):
                item.print()

    def show_all_books(self):
        for item in self.printable_list:
            if isinstance(item, Book):
                item.print()

Main.add(Main,Magazine('Magazine1'))
Main.add(Main, Book('Book1'))
Main.add(Main, Magazine('Magazine3'))
Main.add(Main, Magazine('Magazine2'))
Main.add(Main, Book('Book2'))

Main.show_all_magazines(Main)
print('-' * 40)
Main.show_all_books(Main)
