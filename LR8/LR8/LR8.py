print('Введите предложения, разделяя их знаком "."')
A = input()
B = A.split('.')
del B[-1]
print('Предложения, которые содержат двузначные числа:')
for sentense in B:
    if not(sentense[len(sentense)-3].isdigit()) and sentense[len(sentense)-2].isdigit() and sentense[len(sentense)-1].isdigit():
        print(sentense)
        continue
    for i in range(3, len(sentense)):  
        if not(sentense[i - 3].isdigit()) and sentense[i-2].isdigit() and sentense[i-1].isdigit() and not(sentense[i].isdigit()):
            print(sentense)
            break

#1aa. 11aa. 111aa. aa1aa. aa11aa. aa111aa. aa1. aa11. aa111. aa1111.