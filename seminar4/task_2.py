""" 2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой. """

name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
year = int(input('Ваш год рождения: '))
place = input('Ваш горож проживания: ')
e_mail = input('Ваш e-mail: ')
phone = input('Ваш номер телефона: ')


def my_func(arg_1, arg_2, arg_3, arg_4, arg_5, arg_6):
    result = f'{name} {surname} {year} г.р., г.{place}, ' \
             f'e-mail: {e_mail}, phone: {phone}'
    return result


print(my_func(arg_1=name, arg_2=surname, arg_3=year,
              arg_4=place, arg_5=e_mail, arg_6=phone))
