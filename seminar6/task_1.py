""" 1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами. """

from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, bonus = argv
    time_work = int(time_work)
    rate = int(rate)
    bonus = int(bonus)
    print((time_work * rate) + bonus)
else:
    time_work = int(input("Введите отработанные часы: "))
    rate = int(input("Введите ставку/ч: "))
    bonus = int(input("Введите бонус: "))
    print(time_work * rate + bonus)
