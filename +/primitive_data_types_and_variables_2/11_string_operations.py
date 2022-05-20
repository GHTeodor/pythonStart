str1 = 'hel'
str2 = 'lo'
result = str1 + str2  # конкатенація рядків

print(result)

# форматування рядків
a = 48
b = 73

message1 = '%d + %d = %d' % (a, b, a + b)
print(message1)

message2 = '{} - {} = {}'.format(a, b, a - b)
print(message2)

message2 = f'{a} - {b} = {a - b}'
print(message2)

# індексація рядків
s = 'Hello, World!'

# (повернутись у сьомому уроці)
print(s[0])  # індексація починається з нуля
print(s[4])  # четвертий (п'ятий логічно) елемент (символ)
print(s[-1])  # негативні числа - індексація з кінця

print(s[2:7])  # символи з другого (включно) до п'ятого (не включно)
print(s[2:7:2])  # те саме, але з кроком два
