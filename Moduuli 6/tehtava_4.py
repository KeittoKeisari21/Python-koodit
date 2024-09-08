def laske(x):
    s = 0
    for y in x:
        s = s + y
    return s
x = [1, 2, 3]
s = laske(x)
print(s)