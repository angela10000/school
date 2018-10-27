#задача 1 (гугл в помощь) 

'''import random 
a = str(random.randint(100,999))
print(a, int(a[0]) + int(a[1]) + int (a[2]))

'''#задача 3 

a = int(input('введите год: \n'))
if a % 400 == 0:
    print ('год не является високосным')
elif a % 4 == 0:
    print ('год является високосным')
else:
    print ('год не является високосным')
