# დავალება 1
def nugzar_chubinidze(sadgerdzelo, limit):
    if sadgerdzelo > limit:
        return "ნუგზარი აღარ დალიო მეტი!"
    else:
        return "მოდი ახლა მართლა, დამილოცნიე!"
    
print(nugzar_chubinidze(4, 6))
print(nugzar_chubinidze(7, 6))
print(nugzar_chubinidze(10, 6))
print(nugzar_chubinidze(1, 6))
print(nugzar_chubinidze(9, 6))





# დავალება 2
def yuri_gagarini():
    იურის_წნევა = 120
    იურის_პულსი = 80

    მომხმარებლის_წნევა = int(input("წნევა უდრის: "))
    მომხმარებლის_პულსი = int(input("პულსია: "))

    if იურის_წნევა == მომხმარებლის_წნევა and იურის_პულსი == მომხმარებლის_პულსი:
        return True
    else:
        return False 

print(yuri_gagarini())



# დავალება 3





# დავალება 4
ვაშლის_ლისტი = ["პანტა", "პანტა", "გორული"] 

ვაშლები = set(ვაშლის_ლისტი)

print(ვაშლები)
