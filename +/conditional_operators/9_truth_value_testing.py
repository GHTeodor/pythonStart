string = input('Enter a string: ')
# Те саме, що й if string is not None and string != ''

if string:
    print('The string is {}'.format(string))

number = int(input('Enter a number: '))

if number:
    print('Число не дорівнює нулю')
else:
    print('Число дорівнює нулю')
