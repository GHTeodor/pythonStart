# 1. Розрахувати вартість товару з урахуванням знижки. todo
# Якщо вартість товару більша за 100 грн – знижка 3%.
# Якщо вартість товару більша за 500 грн – знижка 5%.
# Якщо вартість товару більша за 1000 грн – знижка 10%.

price = float(input("Enter price: "))
discount = 0
if price > 1000:
    discount = 10
elif price > 500:
    discount = 5
elif price > 100:
    discount = 3
print(f"Price = {price} ₴\n Your discount = {discount} %")

print(40*"--")

# 2. За допомогою тернарного оператора реалізувати таке завдання: todo
# На вхід отримуємо змінну з рядковим значенням. Якщо це значення — порожній
# рядок, то повернути дефолтне значення None, якщо рядок не порожній —
# повернути його.

inputNone = input("Enter or skip ")
print(inputNone) if inputNone else print(None)

print(40*"--")

# 3. todo
# На вхід подається будь-яке float число. Дізнатися, скільки розрядів у числі (1, 2, 3 або більше)
# до та після коми (крапки) та чи воно додатнє, або від’ємне. Наприклад, 25.1 - це додатнє [2:1],
# а -345,210 - це від’ємне [3:3], а 2400.09 - це додатнє [4:2]. 0 враховувати як окремий варіант.

anyFloat = float(input("Enter value with '.'(dot) [example = 1.1]:_ "))
if anyFloat == 0:
    print(f"You entered {anyFloat}")
else:
    print(f"{anyFloat} is Positive") if anyFloat > 0 else print(f"{anyFloat} is Negative")
    dot = str(abs(anyFloat)).split('.')
    print(f"[{len(dot[0])}:{len(dot[1])}]")
