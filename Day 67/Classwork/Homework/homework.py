# N.1
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"first dog's name is {self.name} and is {self.age} years old, the second one's name is {self.age} and is {self.age} years old."

D1 = Dog("Max", 3)
D2 = Dog("Lucky", 1)

print(D1)
print(D2)


# N.2
