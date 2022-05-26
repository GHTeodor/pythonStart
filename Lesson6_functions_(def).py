print(any([False, 0, '', [], {}, None]))  # all False
print(any(([{}], (('')), 0)))  # True False False === True


def concatenation(a='Default', b='0'):
    print(a + b)


concatenation('Combine', '000')
concatenation()


def pretty_print(quantity, item, price):
    print(f"{quantity} {item} cost {price: .2f}")


pretty_print(5, "bananas", 1.8765)
pretty_print(price=1.8765, quantity=5, item="bananas")
print(40 * "__")


def add_some(my_list=[]):
    my_list += '*'
    print(my_list)


add_some()
add_some()
add_some()
print(40 * "__")


def add_some_correct(my_list=None):
    if my_list is None:
        my_list = []
    my_list += '*'
    print(my_list)


add_some_correct()
add_some_correct()
add_some_correct()
print(40 * "__")


def avg(*args):
    total = 0
    for arg in args:
        if type(arg) is int or type(arg) is float:
            total += arg
        else:
            return f'{args} must be type of number'
    return total / len(args)


print(avg(1.2, 3, 5, 5, 6, 77, 2, 5.1))
t = (11, 22, 33, 44, 55, 66)
print(avg(*t))


def summa(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, '--->', value)


summa(one=1, two=2, username='Tarabarova')
fff = {'first': 12, 'second': 32}
summa(**fff)


def f(a, b, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"**args = {args}")
    print(f"**kwargs = {kwargs}")


f('aaa', 5, 5, 6, 7, 15, dd=667, the='record')


def docs():
    """It is function"""
    pass


print(docs.__doc__)


def func(a: int, b: str) -> float:
    print(a, b)
    return (3.5)


func(1, 'foo')

print(func.__annotations__)
