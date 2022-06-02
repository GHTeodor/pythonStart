a = 123
b = str(a)
print(f"type of a: {type(a)}")
print(f"type of b: {type(b)}")

c = "iterator"
d = list(c)

sss = iter(c)
print(sss)
print('step 1', next(sss))
print('step 2', next(sss))
print('step 3', next(sss))
print(d)

print('bool []:', bool([]), '\nbool [None]:', bool([None]))

f = "AaBbCcDdEe_,.#"
print(f"max: {f}, min: {f}")

g = lambda x, y, z: x + y * z
print(g(1, 2, 3))

l = [
    lambda x: pow(x, 0),
    lambda x: pow(x, 1),
    lambda x: pow(x, 2),
    lambda x: pow(x, 3),
    lambda x: pow(x, 4),
]
for i in l:
    print(i(5))

    def l(x): return pow(x, 0)
    def h(x): return pow(x, 1)
    def t(x): return pow(x, 2)

for i in [l, h, t]:
    print(i(5))


print(40 * '--')


class A:
    def some_method(self):
        print('Spam, eggs!!1')


class B(A):
    def some_method(self):
        super().some_method()
        print('Hello, World!')


B().some_method()
