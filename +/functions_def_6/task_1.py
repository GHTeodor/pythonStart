"""
Написати функцію, яка приймає 2 аргументи – цілі числа. Всередині функції виконується перевірка типу. Якщо хоча б одне з них не
int, то повертається 1, якщо обидва int, то рахується їхня сума. Якщо сума додатня, повертається 0, якщо від’ємна, то -1.
"""

def task_1(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        result = 0 if (a + b) > 0 else -1
        return result
    else:
        return 1

print(task_1(1,3))

print(task_1('dd', 2))

print(task_1(-5, 0))

