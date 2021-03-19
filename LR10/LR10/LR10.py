import math
def f1 (x):
    return math.tan(x)

def f2 (x):
    x = (math.sin(2*x) + math.sin(5*x) - math.sin(3*x)) / (math.cos(2*x) + 1 - math.sin(x)**2)
    return x

reader = open('input.txt','r')
writer = open('output.txt','w')


x = float(reader.read())
writer.write(str(f2(x)) + '\n' + str(f1(x)))
writer.close()
print('Файл перезаписан')


