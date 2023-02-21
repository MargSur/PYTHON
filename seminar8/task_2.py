""" 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке. """

count_line = 0
count_words = 0
count_symbols = 0

with open('for_second_task.txt', 'r', encoding='utf-8') as text:
    for line in text:
        print()
        count_line += 1
        count_words = len(line.split())
        print(f'кол-во слов в строке "{line}" = {count_words}')
        print()
        for el in line.split():
            count_symbols = len(el.strip('\n'))
            print(f'Кол-во символов в слове "{el}" = {count_symbols}')
    print()
    print(f'Кол-во строк в тексте {count_line}')
