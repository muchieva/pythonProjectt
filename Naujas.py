import random
import re

v1 = "Ryan"
p1 = "Reynolds"

if len(v1) > len(p1):
    print(p1)
else:
    print(v1)

v2 = 'Winona'
p2 = 'Ryder'

print(v2.upper() , p2.lower())

v3 = 'Chris'
p3 = 'Hemsworth'

try_pirmos_raides = v3[:3], p3[:3]
print(''.join(try_pirmos_raides))

v4 = 'Marilyn'
p4 = 'Monroe'

trys_paskutines_raides = v4[-3:] , p4[-3:]

print('' .join(trys_paskutines_raides))


string = 'An american in Paris'

new_string = re.sub(r'a', '*', string, flags=re.IGNORECASE)
print(new_string)

result = re.sub(r'[AEIOU]', '', string, flags=re.IGNORECASE)

print(result)

string2 = 'Breakfast at Tiffany\'s'
string2_1 = re.sub(r'[AEIOU]', '', string2, flags=re.IGNORECASE)

print(string2_1)

string3 = '2001: A Space Odyssey'
string3_1 = re.sub(r'[AEIOU]', '', string3, flags=re.IGNORECASE)

print(string3_1)

string4 = 'It\'s a Wonderful Life'

string4_1 = re.sub(r'[AEIOU]', '', string4, flags=re.IGNORECASE)
print(string4_1)

starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"

epizodas = [int(s) for s in starWars.split() if s.isdigit()]

print(starWars [-14])
print(epizodas)

fraze ='Don\'t Be a Menace to South Central While Drinking Your Juice in the Hood'

def num_words(string, length): fraze
count = 0
for word in fraze.split():
    if len(word) <= 5:
        count += 1
print("Zodziu kurie yra sudaryti is 5 ar maziau raidziu yra" , count)

fraze2 = 'Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale'
def num_words(string, length): fraze2
count1 = 0
for word in fraze2.split():
    if len(word) <= 5:
        count1 += 1
print("Zodziu kurie yra sudaryti is 5 ar maziau raidziu yra" , count1)

from string import ascii_lowercase

str = ascii_lowercase

print(''.join(random.choice(str) for _ in range(3)))


zodziai = fraze.split()
print(zodziai)

print((random.sample(zodziai , k=10)))