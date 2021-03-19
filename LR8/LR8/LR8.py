print('Введите предложения, разделяя их знаком "."')
A = input()
B = A.split('.')
print('Предложения, которые содержат двузначные числа:')
for sentense in B:
    for i in range(0,len(sentense)-2):
        if sentense[i].isdigit() and sentense[i+1].isdigit():
            print(sentense)
            break
