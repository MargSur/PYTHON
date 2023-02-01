""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов. """
""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов. """

def my_func(x, y, z):
    sorting = [x, y, z]
    total = []
    max_num1 = max(sorting)
    total.append(max_num1)
    sorting.remove(max_num1)
    max_num2 = max(sorting)
    total.append(max_num2)
    print(sum(total))

my_func(x=14, y=16, z=-5)

