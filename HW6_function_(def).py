# Завдання 1
# Написати функцію, в яку передається аргументом інша функція. Всередині приймаючої функції
# зробіть вивід у консоль “Початок виклику”, після чого викличте функцію і результат виведіть у
# консоль, після чого виведіть у консоль “Кінець виклику”. Для прикладу можете написати функцію
# додавання 2 чисел і передати її в приймаючу функцію.

def call_start(func):
    print("Початок виклику")
    func(1, 2)


def call_end(a, b):
    print(f"{a} + {b} = {a + b}")
    print("Кінець виклику")


call_start(call_end)

print(40 * '--')


# Завдання 2
# Написати функцію, яка повертатиме результат найбільшого спільного дільника двох чисел, переданих у параметри


def max_divider(x, y):
    if isinstance(x, int) and isinstance(y, int):
        if x > y:
            for i in range(y + 1)[:0:-1]:
                if int(x / i) == x / i and int(y / i) == y / i:
                    return i

        elif x < y:
            for i in range(x + 1)[:0:-1]:
                if int(x / i) == x / i and int(y / i) == y / i:
                    return i

        elif x == y:
            return x

    else:
        return "Як мінімум один з аргументів не <int>"


print(max_divider(15, 20))
print(max_divider(-21, 7))
print(max_divider('15', 15))
