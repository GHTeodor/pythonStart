# Функція з минулого прикладу
def print_numbers(limit):
    for i in range(limit):
        print(i)


# Зчитуємо введення користувача за допомогою стандартної
# функції input, конструюємо з нього число
# за допомогою стандартної функції int і записуємо в
# змінну n
n = int(input('Введіть n: '))

# Викликаємо функцію print_numbers із фактичним параметром n
print_numbers(n)