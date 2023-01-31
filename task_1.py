"""
Задание 1.
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.
"""

start = float(input("Введите результаты пробежки первого дня в км: "))
finish = float(input("Введите желаемый результат в км: "))
days = 1
print(days, '-й день:', round(start))

while start <= finish:
        start += start / 10
        days += 1
        print(days, '-й день:', round(start, 2))
else:
        print(f'На {days}-й день спортсмен достиг результата '
              f'— не менее {int(start)} км.')