"""
Написати програму, яка визначає яким є число - парним чи непарним. Якщо залишок від розподілу на 2 не
дорівнює 0, це непарне число, а якщо дорівнює - то парне.
"""

number = float(input("введіть число: "))

if number % 2:
    print("непарне")
else:
    print("парне")