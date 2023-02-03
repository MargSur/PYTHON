""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

# Вариант 1. With SORT

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))


def my_func(arg1, arg2, arg3):
    lst = list()
    lst.append(arg1)
    lst.append(arg2)
    lst.append(arg3)
    lst.sort()
    return lst[1]+lst[2]


print(f'сумма наибольших двух чисел: {my_func(num1, num2, num3)}')