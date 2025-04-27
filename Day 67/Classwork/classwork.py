class Person:
    def __init__(self, name, lastname, father_name):
        self.name = name
        self.lastname = lastname
        self.father_name = father_name

    def __str__(self):
        return f"My name is {self.name}, my lastname is {self.lastname} and my father's name is {self.father_name}."
    
p1 = Person("Nikolozi", "Bliadze", "Cezari")

print(p1)