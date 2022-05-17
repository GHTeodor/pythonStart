from random import randrange
print(3, "--" * 40) # Lesson 3 ========================================================================================

a = randrange(5, 10)
b = randrange(5)
z = 3 if a < b else (1 if a == b else 2)

print(f"a={a}, b={b}, z={z}")

string = 'nAME'.capitalize()
print(string)

print(2, "--" * 40) # Lesson 2 ========================================================================================
# print(r"1\'231'123''1\"")
# # print('Name', input('Enter your name, please: '))
# UKR = "ще не вмерла України і слава, і воля"
# print("і" in UKR)
# print(UKR.capitalize()) # Перша літера велика
# print(UKR.upper()) # .lower()
# print(UKR[-1]) # остання літера
#
# a=1
# print(id(a)==id(1))
#
# print(type(1.2e-3))
# print(type(1_000_000_000))
# print(type(1+5j))
# print(1_00.1e100)
#
# lines = """\
# ... He took his vorpal sword in hand;
# ...       Long time the manxome foe he sought—
# ... So rested he by the Tumtum tree
# ...       And stood awhile in thought.
# ... """
# print(lines.splitlines())


print(1, "--" * 40) # Lesson 1 ========================================================================================
# print('Hello, world!')
# name = input("Введіть своє ім'я, будь ласка: ")
# print('Привіт, ' + name)
# print(f"Привіт, {name}!")