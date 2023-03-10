""" Задание 2.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой. """

from sys import exit


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

try:
    if num2 == 0:
        raise MyError("Ошибка! Вы пытаетесь делить на 0!")
    res = num1 / num2
except MyError as err:
    print(err)
else:
    print(f"Результат деления {num1} на {num2} =", res)
