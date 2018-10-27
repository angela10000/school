'''a = input('Введите число \n')
print (len(a))'''


a = abs(int(input('Введите число \n')))
k = 0
while a > 0 :
    a = a//10
    k = k + 1
print (k)
