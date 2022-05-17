a = 2
b = 5

print(a < b)  # менше
print(b > 3)  # більше
print(a <= 2)  # менше або дорівнює
print(b >= 7)  # більше або дорівнює
print(a < 3 < b)  # подвійне порівняння
print(a == b)  # рівність
print(a != b)  # нерівність
print(a is b)  # ідентичність об'єктів у пам'яті
print(a is not b)  # a і b – різні об'єкти (хоча значення їх можуть бути рівними)

string = "some string"
second_string = string
third_string = input('Введіть рядок: ')

print(string is second_string)
print(string is third_string)
