
import math
def f1 (x):
    return math.tan(x)

def f2 (x):
    x = (math.sin(2*x) + math.sin(5*x) - math.sin(3*x)) / (math.cos(2*x) + 1 - math.sin(x)**2)
    return x

x = float(input())
print(f2(x))
print(f1(x))

