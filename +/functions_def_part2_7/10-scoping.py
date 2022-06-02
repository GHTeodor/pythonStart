def outer_function():
    var = 8  # створення локальної змінної var

    def inner_function():
        # вказує, що необхідно використовувати глобальну змінну
        global var
        print(var)  # 0
        var = 10

    print(var)  # 8
    inner_function()  # виклик внутрішньої функції
    print(var)  # 8


# створення глобальної змінної var
var = 0
print(var)  # 0
outer_function()
print(var)  # 10
