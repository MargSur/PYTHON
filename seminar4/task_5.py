""" 5. Сделайте профилирование кода любого или любых выполненных 
заданий с помощью модуля timeit, опишите результат """

from timeit import timeit

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
print(timeit('my_func', globals=globals(), number=1000000))

# Стоимость использования my_func=0.015979899966623634