import random
import math

#Заполняем список
a = []
for x in range(0,10,1):
    a.append(random.random() * 10 - 5)
for x in a:
    print(x)

#Задание 1
sum = 0
for x in range(0,len(a),2):
    sum += a[x]
print("\nСумма нечетных элементов:", sum)

#Задание 2
sum1 = 0
start = 0
stop = 0
for x in range(0,len(a),1):
    if a[x] < 0:
        start = x
        break
for x in range(len(a)-1,0,-1):
    if a[x] < 0:
        stop = x
        break
for x in range(start + 1, stop, 1):
    sum1 += a[x]
print("\nСумма элементов между ", start, " и ", stop,": ", sum1,"\n")

#Задание 3

for x in range(0,len(a)):
    if abs(a[x]) < 1:
        a.remove(a[x])
        a.append(0)
print("Все числа по модулю меньшие 1 удалены, массив дополнен нулями:")
for x in a:
    print(x)
