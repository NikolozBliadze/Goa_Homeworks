# 1
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Dog('Max', 3)
p2 = Dog("Lucky", 3)
         

print(p1)
print(p2)

# 2
class Car:
    def drive(self):
        print("The car is driving")

    def stop(self):
        print("The car has stopped")

my_car = Car()

my_car.drive()
my_car.stop()



# 3
class Circle:
   def __init__(self, radius):
      self.radius = radius

   def area(self):
        pi = 3.14
        return pi * self.radius ** 2

ci = Circle(5)

print("წრეწირის ფართობია: ", ci.area())

# 4
class Student:
   def __init__(self, name, grade, subject):
      self.name = name
      self.grade = grade
      self.subject = subject

   def introduce(self):
      return f"My name is {self.name}, I study {self.subject} and my grade is {self.grade}."


S1 = Student('Pavle', 9, "History")

print(S1.introduce())


# 5
class Account:
    def __init__(self, balance):
        self.balance = balance

class BankAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} ლარი დაემატა. ახალი ბალანსია: {self.balance} ლარი.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} ლარი გამოთხოვილია. ახალი ბალანსია: {self.balance} ლარი.")
        else:
            print("არასაკმარისი თანხა ბალანსზე.")

account = BankAccount(100)

account.deposit(40)
account.withdraw(20)
account.withdraw(200)