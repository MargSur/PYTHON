""" Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции """

for elements in ['разработка', 'администрирование', 'protocol', 'standard']:
    x = elements.encode('utf-8', 'replace')
    y = x.decode('utf-8')
    print(elements, x, y)