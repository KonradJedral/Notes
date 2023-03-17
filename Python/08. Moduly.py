'''
Moduły


Import modułów 

Żeby zaimportować moduł, wpisujemy “import” plus nazwę modułu, np:
import super_module

możemy również importować tylko wybraną funkcję z całego modułu.
from super_module import super_function

import modułu zawsze zapisujemy na samej górze kodu. 

importując w pierwszy sposób importujemy całą zawartość do podkatalogu i wtedy, żeby użyć funkcji z danego modułu musimy wskazać pythonowi ścieżkę skąd ma brać daną funkcję np:
import math
print(math.pi)		- nie wystarczy samo pi, ponieważ trzeba wskazać ścieżkę, dlatego jest math.(jako lokalizacja funkcji) pi (nazwa funkcji)
Jeśli zaimportujemy w sposób:
from math import *
wtedy wszystkie funkcje są tak jakby wrzucane do głównego folderu ze wszystkimi innymi funkcjami i nie trzeba wskazywać ścieżki dostępu. Wtedy wystarczy napisać:
print(pi)

Uwaga! jeżeli funkcje z różnych modułów mają takie same nazwy to trzeba importować według pierwszego sposobu lub tylko wybrane elementy z modułów, żeby nazwy się nie pokrywały. np sam “from math import pi”
'''

# Moduł String

# Digits
from string import digits
print(digits) 			#  drukuje wszystkie cyfry (0123456789)

capwords

from string import capwords  
input_string = input()
print(capwords(input_string)) 		# Drukuje wszystkie słowa z dużej litery 


# Tabela ASCII - posiada cyfry, litery i znaki specjalne zapisane w formie numerycznej, dzięki modułowi string możemy wyciągać np. listę ASCII z samymi literami

# Moduł math

import math

abs (x) 			# zwraca wartość bezwzględną x 
round (x, 2) 		# zwraca x zaokrąglone do 2 miejsca po przecinku
pow (x, y) 			# zwraca x podniesione do potęgi y;
max (a, b, c, ...)		# zwraca największy argument;
min (a, b, c, ...) 		# zwraca najmniejszy argument.

abs_integer = abs(-10)  # 10
abs_float = abs(-10.0)  # 10.0

round_integer = round(10.0)      # 10, returns integer when ndigits is omitted
round_float = round(10.2573, 2)  # 10.26

pow_integer = pow(2, 10)  # 1024
pow_float = pow(2.0, 10)  # 1024.0

largest = max(1, 2, 3, 4, 5)   # 5
smallest = min(1, 2, 3, 4, 5)  # 1

math.log(pow, x)  		# służy do obliczenia potęgi, do której był podniesiony “x”, że wyszedł wynik “pow”
math.floor (a) 		# zwraca największą liczbę całkowitą mniejszą od a; zaokrągla w dół
math.ceil (a) 		# zwraca najmniejszą liczbę całkowitą większą od a. zaokrągla do góry
math.pow(a, b)		# a do potęgi b
math.factorial(5)		# wpisuje wartość 5!
math.log(10) 		# drukuje naturalny logarytm z 10
math.pi 			 # 3.141592653589793
math.e			 # stała Eulera (podstawa logarytmu naturalnego).	  2.718281828459045
math.sqrt(x)		# pierwiastek z x
math.cos (a) 		# zwraca cosinus radianów;
math.sin (a) 		# zwraca sinus radianów;
math.degrees (a)		#  zwraca kąt a przekształcony z radianów na stopnie;
math.radians (a) 		# zwraca kąt a przekształcony ze stopni na radiany.
math.median_low		# niższa wartość elementu środkowego ( jeśli liczymy medianę liczb parzystych)
math.median_high	# wyższa wartość elementu środkowego 

math_ls = dir(math)
print(math_ls)		# taki zapis wydrukuje wszystkie funkcje moduły math


# Przykład:
import statistics

percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292, 2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248, 3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169, 4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705, 8.740978348, 6.174819567]

# posortuj liste:

percent.sort()
print(percent, "\n")

# Teraz spóbuj wywołać metodę median przekazując do niej jako argument listę percent. 

median = statistics.median(percent)
print(median)

# metoda median_low i median_high 

medianLow = statistics.median_low(percent)
medianHigh = statistics.median_high(percent)

print(medianLow, medianHigh)

# inny zapis

from statistics import *


percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292, 2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248, 3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169, 4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705, 8.740978348, 6.174819567]

# posortuj liste:

percent.sort()
print(percent, "\n")

# Teraz spóbuj wywołać metodę median przekazując do niej jako argument listę percent. 

median = median(percent)
print(median)

# metodę median_low i median_high

medianLow = median_low(percent)
medianHigh = median_high(percent)

print(medianLow, medianHigh)




copysign
from math import copysign  


x, y = map(float, input().split(' '))
print(copysign(x, y))		- przypisuje do wartości x znak z wartości y (+ lub -)


# Przykład:
import math


inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]


#print(len(inputdata))
#print(len(factortable))


if len(inputdata) == len(factortable):
    i = 0
    while i < len(inputdata):
        maxValue = inputdata[i] + factortable[i] * inputdata[i]
        minValue = inputdata[i] - factortable[i] * inputdata[i]
        print(minValue, maxValue)


        minInteger = math.floor(minValue)
        maxInteger = math.ceil(maxValue)
        print(minInteger, "\t", inputdata[i], "\t", maxInteger)


        i += 1
else:
    print("inputdata and factortable need to have equal number of elements")


# Moduł random
import random
print(random.random()) - drukuje losową liczbe w przedziale 0 - 1

random.seed()
# możemy przypisać seed() (ziarno), według którego wybierana będzie pseudolosowa liczba
random.seed(5)
print(random.random())  	# 0.6229016948897019

random.uniform(a, b) 
# zwraca pseudolosową liczbę “float” z przedziału (a, b) 

random.randint(a, b) 
# zwraca pseudolosową liczbę “int” z przedziału (a, b)

random.choice(nazwaListy)
# zwraca pseudolosową wartość z wybranej sekwencji, listy, słowa


random.randrange(a, b, c) 
# zwraca pseudolosową wartość z przedziału (a, b) z przeskokiem o “c”

print(random.randrange(3, 100, 5))  		# 18
print(random.randrange(1, 5))      		 # 2
print(random.randrange(100))       		 # 44

random.shuffle(nazwaListy) 
# miesza wybraną sekwencję (nie działa z niezmiennymi typami danych - krotki)

tiny_list = ['a', 'apple', 'b', 'banana', 'c', 'cat']
random.shuffle(tiny_list)
print(tiny_list)  # ['apple', 'banana', 'a', 'cat', 'b', 'c']

random.sample(population, k)
# zwraca “k”(ilość) pseudolosowych wartości z population.

print(random.sample(range(100), 3))  # [24, 33, 91]
# zwróciło k=3 wartości z przedziału range(100)

random.betavariate(alpha, beta)
# zwraca pseudolosową wartość z przedziału 0 - 1. Alpha i beta mogą być dowolne

import random
random.seed(3)
print(random.betavariate(0.9, 0.1))	# 0.9997528058485836




# Przykład
# losowanie 10 liczb z zakresu 1 - 100


import random


i = 0


while i < 10:
  print(random.randint(1, 100))
  i +=1 


# losowanie nuber1 od 1 - 100, losowanie number2 (1 - 100) i liczenie za którym razem wylosowała się ta sama liczba co w number1

import random

number1 = random.randint(1, 100)
count = 0 
number2 = 0
while number1 != number2:
  number2 = random.randint(1, 100)
  count += 1 
  print(count, number2)

print("Udało się trafić za ", count, "razem")


# Przykład 

import random

countries = [ 
  'Uruguay', 'Russia', 'Saudi Arabia', 'Egypt', 'Spain', 'Portugal', 'Iran', 'Morocco', 'France', 'Denmark', 'Peru', 'Australia', 'Croatia', 'Argentina', 'Nigeria', 'Iceland', 'Brazil', 'Switzerland', 'Serbia', 'Costa Rica', 'Sweden', 'Mexico', 'Korea Republic', 'Germany', 'Belgium', 'England', 'Tunisia', 'Panama', 'Colombia',
 'Japan', 'Senegal', 'Poland' 
]

random.shuffle(countries)
 
groupNumber = 0
 
for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])


# pętla for przyjmuje ilość iteracji według długości listy countries
# najpierw sprawdza, czy i jest podzielne przez 4, jeśli tak to zwiększa group number i drukuje number grupy, jeśli nie to przechodzi do kolejnego polecenia w pętli, czyli print(countries[i]), które jest wykonywane w każdej iteracji, ponieważ jest na tej samej wysokości wcięć co “if”.
# w pierwszej iteracji i przyjmuje wartość 0


# Przykład
import random

min = 1
max = 6 

dices = []

for i in range(5):
  dices.append(random.randint(min, max))
  

dices.sort()
print(dices)

# dodaje i sortuje 5 losowych liczb z zakresu 1 - 6 


Przykład1: (randint / seed)
from random import randint  
from random import seed


n = int(input())


random.randint(-100, 100)	# wybiera losową liczbę z przedziału (a, b)
random.seed(n)			# ustala “ziarno” według którego określany jest 						wynik z przedziału randint()
print(randint(-100, 100))

Przykład2: (seed / choice)
import random


n = int(input())
random.seed(n)
print(random.choice("Voldemort"))

# drukuje pseudolosowo wybrany element (wybrany przez seed(n)) ze słowa “Voldemort”

Przykład3: (seed / shuffle)
import random


sentence = input().split()
random.seed(43)
random.shuffle(sentence)


print(' '.join(sentence))
# drukuje w “sentence” pseudolosowej kolejności. Drukuje jako string, ponieważ drukuje pustego stringa (“ “), do którego dodajemy sentence (“.join(sentence)). Inaczej wydrukowałoby jako listę

# Przykład
import random


inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = random.random()
i = 0


while i < len(inputdata):
    maxValue = inputdata[i] + factortable * inputdata[i]
    minValue = inputdata[i] - factortable * inputdata[i]
    print("min Value = ", minValue, "\nmax Value = ", maxValue)
    i += 1

# Przykład Lotto

# Lotto




import random


myNumbers = []


while len(myNumbers) < 7:


    newNumber = random.randint(1, 49)
    if newNumber in myNumbers:
        print("eliminate: ", newNumber)                     # nie może się dwa razy powtórzyć ta sama liczba, dlatego jeżeli newNumber
        continue                                            # jest juz w liście myNumbers to używamy funkcji continue, żeby pominąć dalsze
    myNumbers.append(newNumber)                             # instrukcje zawarte w pętli. Dlatego w przypadku gdy jest taki sam numer to
                                                            # funkcja append nie jest użyta
print("Whose number will win: ", myNumbers)


# Przykład tasowanie i rozdawanie kart

# Tasowanie kart


import random


colors = ["kier", "karo", "trefl", "dzwonek"]
figures = ["As", "Król", "Dama", "Walet", "10", "9"]


allCards = []


for i in colors:                                # tworzymy wszystkie karty z kolorów i figur
    for j in figures:
        newCard = j + "-" + i
        allCards.append(newCard)


#print(allCards)                                
random.shuffle(allCards)                        # tasujemy karty
#print(allCards)                        


player1 = []                                    # dodajemy graczy
player2 = []
player3 = []    
cardId = 0


while cardId < len(allCards):                   # rozdajemy karty trzem graczom
    pickCard = allCards[cardId]
    if len(player1) > len(player2):
        player2.append(pickCard)
    elif len(player2) > len(player3):
        player3.append(pickCard)
    else:
        player1.append(pickCard)
    cardId += 1


print("Player1 cards = ", player1, "\nPlayer2 cards = ", player2, "\nPlayer3 cards = ", player3)

time
import time
print(time.time)
print("\n")
print(time.localtime(time.time()))                  # time.struct_time(tm_year=2022, tm_mon=10, tm_mday=10, tm_hour=14, tm_min=59, tm_sec=11, tm_wday=0, tm_yday=283, tm_isdst=1)
print("\n")
print(time.asctime(time.localtime(time.time())))    # Mon Oct 10 15:01:59 2022
print("\n")




calendar

import calendar


print(calendar.month(1991, 4, w=5, l=2))            # wyświetla kalendarz z (rok, miesiac, ilość znaków na dzień(miejsca), odstępy pomiędzy liniami)
print("\n")
print(calendar.weekday(1991, 4, 19))                # wyświetla jaki dzień był w podanej dacie (0 - poniedziałek, 1 - wtorek, 2 - środa, itd.)
print("\n")
calendar.setfirstweekday(6)                         # zmieni parametr od którego dnia ma się rysować kalendarz 6 - niedziela
print(calendar.month(1991, 4, w=5, l=2))
print("\n")
print(calendar.isleap(2000))                        # wyświetla, czy rok 2000 był przestępny (True or False)
print("\n")
print(calendar.leapdays(2000, 2020))                # wyświetla, ile było lat przestępnych w zadanym okresie, bez końcowego zakresu (bez 2020) - odp. 5 (2000, 2004, 2008, 2012, 2016)
print("\n")
calendar.setfirstweekday(0)
print(calendar.calendar(2023, w=5, l=2))            # wyświetla kalendarz na podany rok



'''
datatime
datetime.timedelta(days=, hours=, minutes= )
datetime.date(YYYY, MM, DD)
datetime.date.today()
datetime.datetime.now() / today() / utcnow() / today().weekday()
datetime.datetime.now().strftime("%A") / ("%a")
'''



print(datetime.timedelta(days=1, hours=2, minutes=-30)) # timedelta wylicza ile czasu pozostało. odp: 1 day, 1:30:00  (minuty są na minusie)


print(datetime.timedelta(days=-1, hours=-2, minutes=-3))    # wylicza czas również do tyłu. odp: -2 days, 21:57:00


print(datetime.date.today())                        # dzisiejsza data


# przykład wykorzystania, otrzymujemy fakturę, na której zapłacenie mamy 7 dni. dzięki datetime możemy wyznaczyć datę kiedy będzie mijał termin zapłaty:


today = datetime.date.today()
daysToPay = datetime.timedelta(days=7)
print("Today is ", today)
print("Bills should be paid within: ", daysToPay.days, "days")
print("The bill should be paid till: ", today + daysToPay)


# sprawdzamy kiedy będzie koniec świata:


endOfTheWorldByPython = datetime.date.max           # funkcja max pokazuje maksymalny zakres w module datetime.date
print("The final end of the world will happen (by Python): ", endOfTheWorldByPython)
print(endOfTheWorldByPython.weekday())              # sprawdzamy jaki to będzie dzień


# sprawdzamy ile czasu nam jeszcze zostało
today = datetime.date.today()
print(endOfTheWorldByPython - today)


# sprawdzamy ile ktoś żyje


bornDate = datetime.date(1991, 4, 19)
today = datetime.date.today()


print("Żyje ", today - bornDate)


# funkcja datetime z modułu datetime


print(datetime.datetime.now())               # pokazuje aktualna date i czas
print(datetime.datetime.today())             # pokazuje aktualna date i czas
print(datetime.datetime.utcnow())            # pokazuje czas z UTC0
print(datetime.datetime.today().weekday())   # wyświetla aktualny dzień


#konwertowanie czasu na napisy:


print(datetime.datetime.now().strftime("%a"))                   # %a odpowiada za nazwę skróconą dnia (Mon)
print(datetime.datetime.now().strftime("%A"))                   # %A odpowiada za pełną nazwę dnia (Monday)
print(datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")) # Struktura pełnej daty. Rok-Miesiąc-Dzień_Godzina_Minuta_Sekunda_Milisekunda

