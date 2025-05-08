# 1 CodeWars
sum_array = lambda a : sum(a)

# 2
class Info():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

info1 = Info("Nika", "Bliadze", 15)

print(info1.name, info1.surname, info1.age)

# 3
num = 0
while num < 10:
    print("GOA is the best")
    num += 1

# 4 CodeWars
find_average = lambda num : 0 if len(num) == 0 else sum(num) / len(num)

# 5 CodeWars
monkey_count = lambda n : list(range(1, n + 1))