# LEGB: Local -> Enclosing-> Global -> Built-in

# ________________________________________________________________________________________
# x = value
# import module
# from module import name
# def func(): ...
# def func(arg1, arg2, ... argN): ....
# class MyClass: ...
# ________________________________________________________________________________________

def square(base):
    result = pow(base, 2)
    print(f"The square of {base} is {result}")


def cube(base):
    result = pow(base, 3)
    print(f"The cube of {base} is {result}")


square(9)
cube(3)


def outer_func():
    var = 100

    def inner_func():
        print(f"printing var from inner_func(): {var}")
        # var = 200

    inner_func()
    print(f"printing var from outer_func(): {var}")


outer_func()

print(__name__)
print(dir())
