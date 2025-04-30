# N.1
number = lambda num1, num2, num3 : (num1 + num2 + num3) / 3
print(number(5, 10, 15))

# N.2 CodeWars
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

# N.3 CodeWars
positive_sum = lambda number: sum(x for x in number if x > 0)

# N.4 CodeWars
find_smallest_int = lambda num: min(num)

# N.5 CodeWars
count_by = lambda x, n : [x * i for i in range(1, n + 1)]