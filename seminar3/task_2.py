""" 2. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове. """

my_list = input("Введите слова через пробел: ").split(' ')
for i in range(0, len(my_list)):
    print(f'{i + 1}. {my_list[i][:10]}')