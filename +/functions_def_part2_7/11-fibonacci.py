# Числа Фібоначчі - послідовність, в якій перші два числа рівні одиниці,
# а всі наступні — сумі двох попередніх.


def fib(n):
    if n == 1 or n == 2:  # умова виходу
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # рекурсивний виклик


index = int(input('Введіть номер числа Фібоначчі: '))
print(fib(index))