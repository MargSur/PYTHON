""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


# Вариант 1. With SORT
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))


def my_func(arg1, arg2, arg3):
    if arg1 < arg2:
        return arg2 + arg3
    elif arg2 < arg1:
        return arg1 + arg3
    else:
        return arg1 + arg2


print(f'сумма наибольших двух чисел: {my_func(num1, num2, num3)}')
