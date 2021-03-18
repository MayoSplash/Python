#Задание1
def task1(s):
    return s[::-1]
#print(task1(input())) 

#Задание2
def task2(s):
    result = 0
    for c in s:
        if int(c) % 2 == 0:
            result = result + 1
    return result
#print(task2(input()))

#Задание3
def task3(s):
    result = 0
    for c in s:
        if (int(c) % 2 == 0) and (int(c)!=0):
            result = result + 1
    return result
#print(task3(input()))

#Задание4
def task4():
    for i in range(100,1000):
        if (i % 7 == 0) and (task41(i) % 7 == 0):
            print(i)
#Возвращает сумму цифр i
def task41(i):
    sum = 0
    while i > 0:
        digit = i % 10
        sum = sum + digit
        i = i // 10
    return sum
#task4()

#Задание5
def task5(s):
    if len(s) != 3:
        return "Число не трехзначное"
    if s[0] != s[1] and s[1] != s[2] and s[0] != s[2]:
        return "Нет одинаковых цифр"
    else:
        return "Есть одинаковые цифры"
#print(task5(input()))

#Задание6
def task6(s):
    result = 0
    i = int(s)
    max = task61(i)
    while i > 0:
        if i % 10 == max:
            result = result + 1
        i = i // 10
    print("Цифра ", max, " встречается ", result, " раз")
#Возвращает максимальную цифру числа i
def task61(i):
    max = 0
    while i > 0:
        if i % 10 > max:
            max = i % 10
        i = i // 10
    return max
#task6(input())

#Задание7
def task7(s):
    while len(s) != 0:
        if s[0] != s[len(s)-1]:
            return "Не палиндром"
        s = s[1:-1]
    return "Палиндром"
#print(task7(input()))

#Задание8
def task81(i):
    d = 2
    while d * d <= i and i % d != 0:
        d += 1
    return d * d > i
def task8(min, max):
    for i in range(min, max):
        if task81(i):
            print (i, "простое")
        else:
            print (i, "простым не является")
#print(task8(int(input()),int(input())))

def task91(n):
  if n <= 1:
    return n
  else:
    return task91(n-1) + task91(n-2)
#возвращает n-ый член Фибоначчи
def task9(n):
    for i in range(1, int(n)):
        print(task91(i))
task9(input())




def task10_1(r,x,y): #TODO
    if (y*y + x*x <= r):
        return True
    else:
        return False
#print(task10_1(float(input()),float(input()),float(input())))

def task10_2(r,x,y):
    if ((y-r)**2 + (x-r)**2 > r) and ((y+r)**2 + (x+r)**2 > r) and (abs(x) <= r) and (abs(y) <= r):
        return True
    else:
        return False
#print(task10_2(float(input()),float(input()),float(input())))

def task103(r,x,y):
    if ((y*y + x*x <= r) and (y >= 0)) or ((x <= 0) and (y >= -r) and (y <= x)):
        return True
    else:
        return False
#print(task10_3(float(input()),float(input()),float(input())))



