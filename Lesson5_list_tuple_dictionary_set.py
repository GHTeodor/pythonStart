# a = [1, 2, 3, 4]
# print(type(a))
#
# b = list((1, 2, 3, 4))
# print(type(b))
#
# print([a] == [b])  # True
# print(a is b)  # False
# c = a
# print(a is c)  # True
# print([a] is [c])  # False
#
# print(id(a), id(b), id(c))
# print(id(a) is id(c))  # False
# print(id(a) == id(c))  # True

r = ['red', 'yellow', 'blue', 'bread']
func = [print, len]
for i in func:
    for k in r:
        i(k) if i is print else print(i(k))

# print(r[-3:-1])
# print(r[-3:3])
# print(r[::-2])


new_r = r[:]
string_r0 = r[0][:]

print(r is new_r)
print(string_r0 is r[0])
print(r * 2)
print(min(r))

empty = []
empty += 'python'
print(empty)
empty += ['python']
print(empty)

print(40 * "--")

print(type((1, 2, 3, 4)))
print(type((1,)))  # <class 'tuple>
print(type((1)))  # <class 'int>

print(40 * "--")

d = {'a': 1}
print(d['a'])
print(type(d))
d['newKey'] = [1, 23, 4]
print(d.items())
print(d.keys())
print(d.values())

c = {'a': 23, 'x': 12}
d.update(c)
print(d.popitem())
print(d)

print(40 * "--")

s = set('asdasasdfff')

print(type(s))
print(s)
