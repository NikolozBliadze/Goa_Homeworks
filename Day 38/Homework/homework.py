def demonstrate_set_methods():
    my_set = set()

    my_set.add("ნიკა")
    my_set.add("ლუკა")
    my_set.add("მირიანი")
    print( my_set)

    my_set.remove("მირიანი")
    print(my_set)


    popped = my_set.pop()
    print(popped)

    my_set.clear()

    set_a = {"ნიკა", "ლუკა", "მირიანი"}
    set_b = {"მირიანი", "ალე", "დათა"}

    union_set = set_a.union(set_b)
    print(union_set)

    difference_set = set_a.difference(set_b)
    print(difference_set)
demonstrate_set_methods()


def myself():
    ჩემითავი = {
        "სახელი": "ნიკა",
        "გვარი": "ბლიაძე",
        "ასალი": 15,
        "სკოლა": "იტალიური სკოლა"
    }

    გასაღები = ჩემითავი.keys()
    print(გასაღები)
    value = ჩემითავი.values()
    print(value)
    
myself()