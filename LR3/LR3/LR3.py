import math

def f(x):
    if x < 0:
        return (-0.5 * x) - 3
    elif (x >= 0) and (x <= 3):
        return -1 * math.sqrt(9 - x**2)
    elif (x > 3) and (x <= 6):
        return math.sqrt(9 - (x - 6)**2)
    else:
        return 0

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

print("X0: ")
x0 = float(input())
print("X1: ")
x1 = float(input())
print("dX: ")
dx = float(input())

for x in frange(x0,x1,dx):
    print("f(",round(x,3),") = ", round(f(x),3))
