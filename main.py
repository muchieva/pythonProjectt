from statistics import median

print(8*4+2)
print (8*(4+2))
print (48/4)
print(3+6*2)


a = 12
print (a)

b = 7
print(b)

c = a + b
print(c)


x = 11
y = 22
u = 33

suma = x + y + u
skirtumas = x - y - u
sandauga = x * y * u
dalmuo = x / y / u


print(f'{x} + {y} + {u} = {suma}')
print(f'{x} - {y} - {u} = {skirtumas}')
print(f'{x} * {y} * {u} = {sandauga}')
print (f'{x} / {y} / {u} = {dalmuo}')



skaicius1 = 3
skaicius2 = 5

print(skaicius1)
print(skaicius2)
print(skaicius1 + 5)
print(skaicius2 * 2)






sk1 = 36
sk2 = 44
sk3 = 17

if sk1 == sk2:
 print("pirmas ir antras skaicius yra lygus")

if sk2 == sk3:
 print("antras ir trecias skaiciai yra lygus")

if sk1 > sk2:
 print("36 yra daugiau uz 44")

if sk2 > sk3 * 2:
 print("44 yra daugiau uz 34")\

if sk1 %2 == 0:
 print("skaicius yra lyginis")

if sk2 %2 != 0:
 print("skaicius yra nelyginis")

if sk3 > 0:
 print("skaicius yra teigiamas")

if sk1 < 0:
 print("skaicius yra neigiamas")

if sk2 %4 == 0:
 print("skaicius dalinasi is 4")

if sk3 %8 == 0:
 print("skaicius dalinasi is 8")



print("Iveskite savo amziu")

amzius = 21

if amzius >= 18:
 print("jus galite balsuoti")



p1 = 6
p2 = 8
p3 = 3

vidurkis = p1 + p2 + p3 / 3

if vidurkis >= 5:
 print("vidurkis teigiamas")



kintamasis = 35
kintamasis2 = 6


if kintamasis %5 == 0:
 print({kintamasis * 1} , {kintamasis * 2} , {kintamasis * 3}, {kintamasis * 4} , {kintamasis * 5})

if kintamasis %2 == 0:
 print({kintamasis} , {kintamasis ** 2} , {kintamasis / 2} )

if kintamasis %7 != 0:
 print({kintamasis + kintamasis2} , {kintamasis - kintamasis2} , {kintamasis * kintamasis2} , {kintamasis / kintamasis2})



pirmas = 6
antras = 7
trecias = 12

if pirmas > antras:
 print ("pirmas didesnis uz antra")
elif antras > trecias:
 print("antras didesnis uz trecia")
elif trecias > pirmas:
 print("trecias didesnis uz pirma")



k1 = 53
k2 = 12
k3 = 82

if k1 == k2:
 print("pirmi du skaiciai yra lygus")
elif k2 == k3:
 print("paskutiniai du skaiciai yra lygus")
elif k1 == 0:
 print("pirmas skaicius yra lygus 0")
elif k2 < 0:
 print("antras skaicius yra neigiamas")
elif k3 > 0:
 print("trecias skaicius yra teigiamas")


pazymys = 8

if pazymys == 10:
 print("puiku")
elif pazymys >= 9:
 print ("labai gerai")
elif pazymys >= 7:
 print (" gerai")
elif pazymys >= 5:
 print ("patenkinamai")
elif pazymys < 5:
 print ("egzaminas neislaikytas")




ivestasis =6

if ivestasis %2 == 0:
 print("skaicius yra lyginis")
elif ivestasis %5 == 0:
 print("skaicius dalinasi is 5")
elif ivestasis == 3:
 print("skaicius yra lygus 3")
else:
 print("Klaida - ivestasis netinkamas")



v1 = 81
v2 = 77
v3 = 91

if v1 == v2:
 print("pirmi du skaiciai yra lygus")
elif v3 > v1:
 print("treciasis skaicius yra didesnis uz pirmaji")
elif v2 == v3 * 2:
 print("yra lygybe")
elif v1 %3 == 0:
 print("pirmas skaicius dalinasi is 3")
else:
 print("Klaida!")

#vienas = int(input())
#du = int(input())
#trys = int(input())

#if vienas >= du and vienas >= trys:
 #print("vienas yra didziausias")
#elif du >= vienas and du >= trys:
 #print ("du yra didziausias")
#elif trys >= vienas and trys >= du:
 #print("trys yra didziausias")


#x1 = int(input())
#x2 = int(input())
#x3 = int(input())

#if x1 <= x2 and x1 <= x3:
 #print(" x1 yra maziausias")
#elif x2 <= x1 and x2 <= x3:
 #print(" x2 yra maziausias")
#elif x3 <= x1 and x3 <= x2:
 #print("x3 yra maziausias")


egzrez1 = 8
egzrez2 = 10
egzrez3 = 7

vidurkis = median([egzrez1, egzrez2, egzrez3])

if vidurkis == 8 or vidurkis > 8:
 print("Labai gerai")
elif vidurkis < 8 or vidurkis > 5:
 print("patenkinamai")
elif vidurkis < 5:
 print("neislaikyta")



ivestsk = int(input())

if ivestsk %2 == 0:
 print("lyginis")
else:
 print("nelyginis")


pasirinkimas = int(input())

if pasirinkimas %7 == 0:
 print("dalinasi is 7")
else:
 print("nesidalina is 7")



file = 'mokymuplanas.doc'

if file.endswith (".py"):
 print("python file")
else:
 print("doc file")

thing1 = 43
thing2 = 65

if thing1 > thing2 or thing1 == 0:
 print("suveike")
if thing2 > thing1 or thing2 == 5:
 print("pavyko")
if thing1 > thing2 and thing1 == 20:
 print("success")
if thing2 > thing1 and thing2 < 100:
 print("completed")



