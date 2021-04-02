import random
#Заполняем массив размера a на b
a = 5

A = []
for i in range(a):
    A.append([])
    for j in range(a):
        A[i].append(random.randint(-1,9))

#Печатаем массив
for i in A:
    for j in i:
        print(j, end=' ')
    print()


#Задание 1
print('\nЗадание 1:')
#Создаем массив для хранения результатов
result = []
for i in range(a):
    result.append(1)

#Проходим по каждой строке для анализа элементов
for i in range(a):
    A.append([])
    for j in range(a):
        if A[i][j] >= 0:
            result[i] *= A[i][j]
        else:
            result[i] = '-'
            break

print(result)

#Звдание 2
print('Задание 2:')
max_sum = A[0][-1]

i = 1
t1 = 0
t2 = 0
for j in range(a-i):
    t1 += A[i+j][j]
    t2 += A[j][i+j]

if t1 > t2: 
    max_sum = t1
else:
    max_sum = t2
print(max_sum)