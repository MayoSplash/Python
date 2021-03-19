def Task1(N):
    if N % 2 == 1:
        return Task1(N-1)
    elif N <= 2:
        return 2
    else:
        return N * Task1(N-2)

def Task2_(M, A):
    if len(A) != 0:
        if A[0] < M:
            M = A[0]
        del A[0]
        return Task2_(M, A)
    else:
        return M


def Task2(A):
    return Task2_(999, A)

print('Задание 1')
print('Произведение четных чисел от 2 до N')
print('Введите N:')
N = int(input())
print(Task1(N))

print('\nЗадание 2')
print('Минимальный элемент массива')
A = []
import random
for i in range(0,15):
    A.append(random.randint(-256,256))
print(A)
print(Task2(A))