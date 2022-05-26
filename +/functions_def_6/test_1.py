def f():
    print("I`m in f-function")

f()

def summa(a, b):
    print(a + b)

summa(5, 10)

summa('ssssss', 'fffffff')

def pretty_print(qty, item, price):
    print(f"{qty}  {item}  cost  ${price:.2f}")

pretty_print(6, 'bananas', 1.8888888)

pretty_print("bananas", 6, 1.888888)


pretty_print(price=1.88888, qty=6, item="bananas")

pretty_print(6, price=1.888888, item="bananas")


def pretty_print_1(qty=6,
                 item="bananas",
                 price=1.88):
    print(f"{qty}  {item}  cost  ${price:.2f}")


pretty_print_1()

pretty_print_1(item="strowberry")

def add_some(my_list=[]):
    my_list.append("###")
    return my_list

print(add_some())

print(add_some())

print(add_some())

def avg(*args):
    total = 0
    for v in args:
        total += v
    return total / len(args)

print(avg(34, 67, 154, 55))

t = (11, 22, 33, 55, 89)

print(avg(*t))

def summmm(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
        print(key, ' ---> ', val)



summmm(one=1, two=2, name='Dima')

fff = {'first': 12, 'second': 32}
summmm(**fff)

def f(a: str, b: int, *args, **kwargs)-> None:
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

f('aaa', 5, 5, 6, 7, 15, dd=6667, hhh="hhhhhh")

def ggg(x, y, z):
    """It is function."""
    pass

print(ggg.__doc__)

