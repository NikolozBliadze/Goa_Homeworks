# N.1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"Car brand is {self.brand}, model is {self.model}, and it was made in {self.year}."


c1 = Car("Tesla", "S", 2023)
print(c1.car_info())


# N.2
class Student:
    def __init__(self, age, grade):
        self.age = age
        self.grade = grade

    def is_passing(self):
        if self.grade > 5:
            return True
        else:
            return False
g1 = Student(15, 8)
print(g1.is_passing())


# N.3
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"Woof!"
    
d1 = Dog("Lucky", 3)
print(d1.bark())

# N.4
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
r1 = rectangle(20, 30)
print(r1.area())

# N.5
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def BookInfo(self):
        return f"Title of the book is {self.title}, author of the book is {self.author} and the year of publication of the book is {self.year}."
    
b1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997)

print(b1.BookInfo())