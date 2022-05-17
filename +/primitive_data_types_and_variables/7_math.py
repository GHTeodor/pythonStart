import math  # імпротуємо модуль math

x = 3.265
# ціле число, найближче ціле знизу, найближче ціле зверху
print(math.trunc(x), math.floor(x), math.ceil(x))

print(math.pi)  # константа пі
print(math.e)  # число Ейлера

y = math.sin(math.pi / 4)  # math.sin – синус
print(round(y, 2))

y = 1 / math.sqrt(2)  # math.sqrt – квадратний корінь
print(round(y, 2))
