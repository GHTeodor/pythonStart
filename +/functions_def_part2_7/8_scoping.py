def function(c, d):
    # a, b - глобальні змінні; c, d - локальні
    global a, b

    # зміна значення глобальної змінної
    a = 5

    # зміна значення глобальної змінної
    b = 7

    # створення локальної змінної з тим самим ім'ям, що й у глобальної
    c = 10

    # створення локальної змінної з тим самим ім'ям, що й у глобальної
    d = 12


a, b, c, d = 1, 2, 3, 4  # множинне привласнення
print(a, b, c, d)  # 1 2 3 4
function(c, d)
print(a, b, c, d)  # 5 7 3 4
