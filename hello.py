

def f(a, b):
    if b == 0:
        print(a)
    else:
        f(b, a%b)
a, b = 10,3
print(f(a, b))


