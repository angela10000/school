a = int(input('Введите год рождения \n'))
b = int(input('Введите год смерти \n'))
c = int(input('Введите кратность \n'))
k = 0
while a <= b:
    if a % c == 0:
        k= k+1
    a= a+1
print (k)

