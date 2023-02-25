""" Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т """

""" class Road:
    def __init__(self, a_len, a_width):
        self._length = a_len
        self._width = a_width

    def a_mass (self, a_weigh, a_thickness):
        return self._length * self._width * a_weigh * a_thickness """


class Road:

    weight = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length  # длина в метрах
        self._width = width  # ширина в метрах

    def mass_calculation(self):
        print(
            f'Масса асфальта равна: '
            f'{int((self._length * self._width * self.weight * self.thickness) / 1000)} '
            f'т')


instance = Road(20, 5000)
instance.mass_calculation()
