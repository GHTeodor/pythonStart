"""
У реченні “Hello world” замінити всі літери “o” на “a”, а літери “l” на “e”
"""

a = "Hello world"
result = ""
for char in a:
    if char == "o":
        result = result + "a"
    elif char == "l":
        result = result + "e"
    else:
        result = result + char

print(result)

print(a[2])
print(len(a))