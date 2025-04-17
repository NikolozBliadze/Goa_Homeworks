def manual_difference():
    difference = set1 - set2
    print(difference)

set1 = {"apple", "banana", "orange", "grape"}
set2 = {"apple", "mango", "pineapple", "cherry"}

manual_difference()




student1 = {
    "name": "ნიკოლოზ",
    "surname": "ბლიაძე",
    "age": 15,
    "average_grade": 10
}

student2 = {
    "name": "ლუკა",
    "surname": "გიორგაძე",
    "age": 14,
    "average_grade": 9
}


print("მოსწავლის 1 ინფორმაცია:")
print(student1.get("name"))
print(student1.get("surname"))
print(student1.get("age"))
print(student1.get("average_grade"))

print("მოსწავლის 2 ინფორმაცია:")
print(student2.get("name"))
print(student2.get("surname"))
print(student2.get("age"))
print(student2.get("average_grade"))