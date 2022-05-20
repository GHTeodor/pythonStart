"""
Вивести у консоль перші 100 чисел Фібоначчі (див. у рекомендованих ресурсах)
wikiwand.com/uk/Послідовність_Фібоначчі
start = 0
"""

start, prev = 0, 1
for i in range(100):
    print(start)
    fibN = start + prev
    # print(f"{str(start)}|{str(prev)}|{str(fibN)}")
    start = prev
    prev = fibN
    # print(f"{str(start)}|{str(prev)}|{str(fibN)}")