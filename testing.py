import statistics
from itertools import count
from random import random, randint

vardas = 'Ieva'
pavarde = 'Muchina'
gimmetai = 1995
siemetai = 2024

print("As esu", vardas, pavarde,"man yra", siemetai - gimmetai , "metai")

a = randint(0,4)
b = randint(0,4)
print(a, b)

if a > b:
    print(round( a / b , 2))
elif a < b:
    print(round( b / a , 2))

x = randint(0,25)
y = randint(0,25)
z = randint (0,25)

print(x, y, z)
if y <= x <= z or z <= x <= y:
    print(x)
elif x <= y <= z or z <= y <= x:
   print(y)
else:
    print(z)

k1 = randint(1,10)
k2 = randint(1,10)
k3 = randint(1,10)

print(k1, k2, k3)

if k1**2 == k2**2 + k3**2 or k2**2 == k1**2 + k3**2 or k3**2 == k1**2 + k2**2:
    print("statusis trikampis")
elif k1**2 < k2**2 + k3**2 or k2**2 < k1**2 + k3**2 or k3**2 < k1**2 + k2**2:
    print("smailusis trikampis")
elif k1**2 > k2**2 + k3**2 and k1 < k2 + k3 or k2**2 > k1**2 + k3**2  and k2 < k1 + k3 or k3**2 > k1**2 + k2**2 and k3 < k1 + k2:
    print("bukasis trikampis")
else:
    print("trikampis nesigauna")



p1 = randint(0,2)
p2 = randint(0,2)
p3 = randint(0,2)
p4 = randint(0,2)

print(p1, p2, p3, p4)

nuliai = 0
vienetai = 1
dvejetai = 2

if p1 == 0:
    print(nuliai)
if p2 == 0:
    print(nuliai)
if p3 == 0:
    print(nuliai)
if p4 == 0:
    print(nuliai)


if p1 == 1:
    print(vienetai)
if p2 == 1:
    print(vienetai)
if p3 == 1:
    print(vienetai)
if p4 == 1:
    print(vienetai)


if p1 == 2:
    print(dvejetai)
if p2 == 2:
    print(dvejetai)
if p3 == 2:
    print(dvejetai)
if p4 == 2:
    print(dvejetai)


o1 = randint(-10,10)
o2 = randint(-10,10)
o3 = randint(-10,10)

if o1 > 0:
    print("[", o1, "]")
elif o1 == 0:
    print("(", o1 , ")")
elif o1 < 0:
    print("{", o1 , "}")

if o2 > 0:
    print("[", o2, "]")
elif o2 == 0:
    print("(", o2, ")")
elif o2 < 0:
    print("{", o2 , "}")

if o3 > 0:
    print("[", o3, "]")
elif o3 == 0:
    print("(", o3 , ")")
elif o3 < 0:
    print("{", o3 , "}")

kiekis = randint(5 , 3000)
kaina = 1

galutine_kaina1 = kaina - (kaina * 0.03)
galutine_kaina2 = kaina - (kaina * 0.04)
print(galutine_kaina2)
print(galutine_kaina1)

print(kiekis)

if kiekis >= 1000 and kiekis < 2000:
    print("Galutine kaina" , galutine_kaina1 * kiekis)

elif kiekis >= 2000:
    print("Galutine kaina" , galutine_kaina2 * kiekis)

else:
    print("Galutine kaina" , kaina * kiekis)


s1 = randint(0 , 100)
s2 = randint(0 , 100)
s3 = randint(0 , 100)

print(s1 , s2, s3)

print(round(statistics.mean( [s1, s2, s3]) , 2 ))

if s1
