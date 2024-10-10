from random import random, randint

vardas = 'Ieva'
pavarde = 'Muchina'
gimmetai = 1995
siemetai = 2024

print("As esu", vardas, pavarde,"man yra", siemetai - gimmetai , "metai")

a = randint(0,4)
b = randint(0,4)

if a > b:
    print(round( a / b , 2))
elif a < b:
    print(round( b / a , 2))

x = randint(0,25)
y = randint(0,25)
z = randint (0,25)

if y <= x <= z or z <= x <= y:
    print(x)
elif x <= y <= z or z <= y <= x:
   print(y)
else:
    print(z)

k1 = randint(1,10)
k2 = randint(1,10)
k3 = randint(1,10)

