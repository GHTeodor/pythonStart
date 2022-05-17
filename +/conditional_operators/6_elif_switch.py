print('''
Меню:
1. Файл
2. Вигляд
3. Вихід
''')

choice = int(input('Ваш вибір: '))

if choice == 1:
    print('Ви обрали пункт меню "Файл"')
elif choice == 2:
    print('Ви відкрили меню "Вигляд"')
elif choice == 3:
    print('Завершення.')
else:
    print('Некоректний вибір')