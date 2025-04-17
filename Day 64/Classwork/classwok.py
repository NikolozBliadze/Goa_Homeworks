# N.1
class human:
  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age

p1 = human("Nika", "bliadze", 15)

print(p1.name, p1.surname, p1.age)




# N.2

class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"ჩემი სახელია {self.first_name}, ჩემი გვარია {self.last_name}, ჩემი ასაკია {self.age}"
    
p1 = Human("ნიკა", "ბლიაძე", 15)

print(p1)
