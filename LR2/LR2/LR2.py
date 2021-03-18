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
print("X: ")
x = float(input())
print("Y: ")
print(f(x))
