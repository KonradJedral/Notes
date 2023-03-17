'''

Pętle

if - jeżeli jest lub nie jest spełniony warunek
while - dopóki jest spełniony określony warunek
for - dla wszystkich elementów danego zbioru danych (listy, krotki itd.)

'''

''' if

 pętla if jest wykonywana jeżeli warunek w niej zapisany jest prawdziwy

składnia:
if zmienna warunek logiczny wartość:
instrukcja zawarta w pętli musi być wcięta “TAB”

'''

# przykład:
age = 23 

if age >= 18:
	print(“You are adult and you can buy alcohol”

# taki zapis wyświetli napis jeżeli age będzie większy niż 18, jeżeli będzie mniejszy nie stanie się nic. Żeby to zmienić trzeba uwzględnić taką sytuację

age = 16 

if age >= 18:
	print(“You are adult and you can buy alcohol”
else:
	print(“You are too young to buy alkohol”)

# możemy dodawać więcej różnych warunków:

age = 16
isDrunk = False 

if age >= 18 and not isDrunk:			
	print(“You are adult and you can buy alcohol”
else:
	print(“Sorry we cannot sell you alkohol”)

# Zostanie wyświetlone “Sorry we cannot sell you alkohol”, ponieważ przynajmniej jeden z warunków nie został spełniony (age)
# PS. and isDrunk żądałby wartości True, natomiast and not isDrunk żąda wartości False


# Przykład 1:
# Pracujesz dla firmy odzieżowej, której celem jest wypromowanie nowej kolekcji ubrań. Firma ogłosiła konkurs, który ma na celu zdobywanie "lajków" i "udostępnień" na Facebooku. Jeśli strona firmy otrzyma danego dnia co najmniej 500 "lajków" i co najmniej 100 "udostępnień", to ceny spadną o 10%. Na razie masz napisać fragment programu, który rozstrzygnie czy warunki promocji są spełnione czy nie.

minLikes = 500
minShares = 100

numLikes = 300
numShares = 107


if numLikes >= minLikes and numShares >= minShares:
  print("Ceny spały o 10%")
else:
  print("Ceny są normale")
 

# Przykład 2:
# Pracujesz dla restauracji, która chce nagrodzić klientów zamawiających w dni robocze (poza weekendem) pizze lub duży napój. Klienci spełniający warunki promocji dostaną kupon na darmowego burgera. Na razie piszesz polecenie decydujące o spełnieniu warunków promocji. Do dyspozycji masz zmienne:
isPizzaOrdered = True
isBigDrinkOrdered = False			#zmienne, które sami zmieniamy
isWeekend = True

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
  print("Otrzymujesz kupon na Burgera")
else:
  print("Zapraszamy ponownie")


# Przykład 3:
# Twój zespół opracowuje przeglądarkę internetową w Pythonie! Twoim zadaniem jest sprawdzenie, czy operacja pobierania pliku na dysk ma się szansę udać, czy jest od razu skazana na porażkę ze względu na brak miejsca na dysku. Na wejściu masz następujące zmienne:
diskSize = 140
diskSizeUsed = 134
fileSize = 5

if fileSize + diskSizeUsed <= diskSize:
  print("Pobieranie pliku")
else:
  print("Brak miejsca na dysku")

# Przykład:
isPizzaOrdered = True
isWeekend = True
isBigDrinkOrdered = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:

	print('Burger for FREE!!!')

elif isWeekend:

	print('Come back on non-Weekend day')

else:

	print('You need to order Pizza or Big drink to have a Burger coupon')



if i elseif (elif) 


# w przypadku kiedy mamy kilka warunków do spełnienia i w zależności od niespełnienia warunku chcemy wyświetlić inny komunikat lub wykonać inną czynność.

age = 22
isDrunk = False
isRestrictedArea = False

if age < 18:
  print("You are to young to buy alkohole")
elif isDrunk:
  print("Are you drunk? We cannot sell you alkohole")
elif isRestrictedArea:
  print("Restricted area. Alcohol is forbidden")
else:
  print("Ok. you can buy alkohole")

# Przykład:
likes = 400
shares = 110

if likes < 500:
  print("Mamy za mało lajków")
elif shares < 100:
  print("Mamy za mało udostępnień")
else:
  print("zniżka 10% aktywowana")

# Przykład:
isPizzaOrdered = True
isWeekend = True
isBigDrinkOrdered = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
	print('Burger for FREE!!!')
elif isWeekend:
	print('Come back on non-Weekend day')
else:
	print('You need to order Pizza or Big drink to have a Burger coupon')


if ternary:

# pętla if zapisana w jednym wierszu dla skrócenia polecenia 

itRains = True

print(“we stay at home” if itRains else “we go out”)
# wydrukuj “we stay at home” jeżeli itRains jest prawdziwe, w innym wypadku wydrukuj “we go out”. Takie polecenie to to samo co:

if itRains:
	print(“we stay at home”)
else:
	print(“we go out:)

# Przykład:
musclePain = True
fever = False
weakness = True

print("suspicion of influenza" if musclePain and fever and weakness else "The flu is unlikely")

if musclePain and fever and weakness:
  print("suspicion of influenza")
elif weakness and (fever or musclePain):
  print("Just take a rest!")
else:
  print("You may be cold")


# while:
# Wykonuje się dopóki warunek pętli jest spełniony
 
# przyład:
i = 0
while i < 5:
    print(i)
    i += 1 
# pętla wydrukuje 0 i na końcu pętli doda 1 do i ( i += 1), następnie pętla będzie wykonywana do momentu, dopóki i < 5. Wynik:
0
1
2
3
4


# Można wykorzystać pętlę z True

i = 0
while True
    if i > 5:
        print("To jest koniec petli")
        break
    else:
        print(i)
        i += 1


# Przykłady z Udemy:
# Wyświetl napis “Row number 1” zwiększając o 1 aż do “Row number 31”.

firstRow = 1
lastRow = 31

while firstRow <= lastRow:
  print("Row number", firstRow)
  firstRow+=1
 

#  Śni Ci się koszmar. Twój nauczyciel matematyki kazał Ci wypisać liczby od 1 do 13 i dla każdej liczby wyliczyć jej kwadrat i sześcian. Ponieważ nauczyciel nie zabronił używać Pythona, napisz pętlę, która dla liczb od 1 do 13 wyświetli kwadrat i sześcian tej liczby

number=1
maxnumber=13

while number <= maxnumber:
  print("kwadrat z", number, "=", number*number)
  print("szescian z", number, "=", number*number*number)
  number+=1


''' Tym razem Twoja Babcia poprosiła Cię o wydrukowanie wzoru haftu krzyżykowego w następującej postaci:
x
xx
xxx
xxxx
xxxxx
xxxxxx
xxxxxxx
xxxxxxxx
xxxxxxxxx
xxxxxxxxxx
'''
'''Babcia woli jednak przechowywać te wzory w postaci skryptów Pythona zamiast gotowych plików tekstowych ze wzorkiem, bo jak twierdzi "Skrypty zajmują w komputerze mniej bajtów - cokolwiek by to było".
Napisz pętlę while, która wygeneruje taki napis składający się z liter 'x' powielanych wiele razy.
'''

number = 1
while number <= 10:
  print(number*'x')
  number+=1



# z podanej listy “values” znajdź wszystkie zestawy 3 następujących po sobie liczb, które są rosnące.

values=[10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

i=0
max = len(values)-3	
		
#max = długość listy values minus 3, ponieważ musimy cofnąć tak, żeby sprawdzanie 3 kolejnych liczb nie wyszło poza listę i nie wzięło 74,puste,puste

while i<max:
	print(i, values[i], values[i+1], values[i+2])	
#wyświetli po kolei numery indexów badanych wartości i 3 następujące po sobie wartości.

	if values[i]<values[i+1] and values[i+1]<values[i+2]:
		print(“\tFound: ‘, values[i], values[i+1], values[i+2])
	i+=1


# Dana jest zakodowana informacja w postaci tabeli:
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
# Trzeba odnaleźć takie dwie kolejne liczby, że druga jest kwadratem pierwszej. W tym celu:
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]


i=0
imax=len(numbers)-1


while i<imax:
  if numbers[i+1] == numbers[i]*numbers[i]:
	print("Found: ", numbers[i], numbers[i+1])
  i+=1




# Tym razem należy analizować po 3 wartości na raz. Interesuje nas odnalezienie takich 3 liczb, że pierwsza do kwadratu równa się drugiej, a druga do kwadratu równa się trzeciej.


numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i=0
imax=len(numbers)-2

while i<imax:
  if numbers[i+1] == numbers[i]*numbers[i] and numbers[i+2] == numbers[i+1]*numbers[i+1]:
	print("Found: ", numbers[i], numbers[i+1], numbers[i+2])
  i+=1


# Twoim zadaniem jest znalezienie takich par kolejnych napisów z tej listy, że długość pierwszego jest równa długości drugiego, np, długość napisu "one" to 3, długość napisu "two" to 3, więc taka para powinna być odnaleziona. Z kolei długość napisu 'two' to 3, a długość napisu "three" to 5, więc taka para nie jest rozwiązaniem.

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i=0
imax=len(texts)-1

while i < imax:
  if len(texts[i]) == len(texts[i+1]):
	print("Taka sama długość ", texts[i], "oraz ", texts[i+1])
  i+=1

# Gra gdzie strzelasz w losowo wybraną przez generator liczbę.

import random

myNumber = random.randint(0, 20)
guessNumber = -1
tryNumber = 0
while guessNumber!=myNumber:
  guessNumber = int(input())
  tryNumber+=1
  if guessNumber>myNumber:
	print(guessNumber, "- Ta liczba jest zbyt duża")
  elif guessNumber<myNumber:
	print(guessNumber, "- Ta liczba jest zbyt mała")
else:
  print("Brawo, ta liczba to:", guessNumber, ", zgadłeś za:", tryNumber, "razem")


# for

# składnia:
for zmienna in zbiór:		
#zmienna - zmienna, która przyjmuje wartości zawarte w zbiorze
#zbiór - lista, krotka, słownik itd

persons = [“Elizabeth”, “Steven”, “Sebastian”, “Margaret”, Svetlana”, “Margaret”]

for person in persons:

# person - przyjmuje wartości Elizabeth, Steven, Sebastian itd. zmieniając swoją wartość z każdym kolejnym wykonaniem pętli, aż do ostatniego elementu.
# persons - nazwa listy

# Przykład 
# przypisanie adresu email dla pracownika:

persons = [“Elizabeth”, “Steven”, “Sebastian”, “Margaret”, Svetlana”, “Margaret”]
domain = “mycompany.com”

for person in persons:
	email = person + “@” + domain
	print(“Email for\t”, person, “\tis\t”, email)	#\t - wcięcia TAB
else:
	print(“end of the list”)

# instrukcja zawarta w else wyświetli informacje jak skończą się elementy listy


# Przykład 1.

# Dana jest lista:
data = ['Error:File cannot be open',
       'Error:No free space on disk',
       'Error:File missing',
       'Warning:Internet connection lost',
       'Error:Access denied']
# Napisz pętlę for, która wyświetli elementy tej listy jeden po drugim. Podczas wyświetlania elementów konwertuj napisy do wielkich liter.
data = ['Error:File cannot be open',
    	'Error:No free space on disk',
    	'Error:File missing',
    	'Warning:Internet connection lost',
    	'Error:Access denied']

for error in data:
  print(error.upper())

# Przykład 2.

# do danych z powyższego przykładu

# Jak widzisz, każdy z elementów listy zawiera znak ":".
# W pętli for każdy z przetwarzanych napisów rozbij ze względu na ":" korzystając z funkcji split.
# Wynik zapamiętaj w nowej dwuelementowej liście elements.
# Następnie wyświetl elements[0] konwertując napis do wielkich liter, a elements[1] wyświetl bez żadnej konwersji


for error in data:
 
  dataList = error.split(":")
  print(dataList[0].upper(), dataList[1])

# Przykład 3.
# 	Te same dane:


# Jeżeli w elements[0] znajduje się napis "Error", wyświetl elements[1] konwertując tekst do wielkich liter
# w przeciwnym razie wyświetl elements[1] bez żadnej konwersji
data = ['Error:File cannot be open',
    	'Error:No free space on disk',
    	'Error:File missing',
    	'Warning:Internet connection lost',
    	'Error:Access denied']

for error in data:
 
  dataList = error.split(":")
  if "Error" in dataList[0]:
	print(dataList[1].upper())
  else:
	print(dataList[1])







# Range
# funkcja range określa do jakiej wartości wykonywać daną pętlę.

for number in range(20)		#wydrukuje liczby od zera do 19 
for number in range(1, 21)		# wydrukuje liczby od 1 do 20 
for number in range(1, 21, 3)	# wydrukuje liczby od 1 do 20 skacząc co 3

# Przykład 1.
# Dane są następujące napisy:
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'
'''Korzystając z polecenia FOR wyświetl:
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
'''

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(10):				# i - dowolna nazwa zmiennej 
  print(string_A)

'''
Przykład 2.
Dane z powyższego
 Korzystając z polecenia FOR wyświetl:
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
'''

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'



for i in range(9):
  if i%2 == 0:
	print(string_A)
  else:
	print(string_B)



# Przykład 3.
# Wyznacz silnie od 1 do 10

a = 1
for i in range(1,11):
  a = i * a
  print(str(i) + "! = " + str(a))


# Pętla zagnieżdżona:

# Masz liczbę rzeczowników i przymiotników:
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
# Utwórz pętlę for iterującą przez listę rzeczowników i zagnieżdżoną w niej pętlę for iterującą przez listę przymiotników. Wyświetl wszystkie pary przymiotnik - rzeczownik
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']


for noun in list_noun:
  for adj in list_adj:
	print(adj, noun)



# Break:

# funkcja break służy do zatrzymania pętli for lub while


# Przykład 
# szukanie liczb pierwszych

for candidate in range(2,31):
	for divider in range(2, candidate):
    	if candidate % divider == 0:
        	print("%2d is not a prime number - divider is %2d" % (candidate, divider))
        	break
	else:
    	print("%2dis prime!" % (candidate))



# w tym przykładzie najpierw pod candidate bierzemy cyfre 2, później pod divider przyjmujemy pierwszą możliwą liczbę od (2, candidate) od 2 do 2-1, nie ma żadnej liczby w tym przedziale, więc wykonuje sie pętla else. 
# Następnie bierzemy candidate = 3 i divider = 2 i sprawdzamy, czy reszta z dzielenia 3/2 jest = 0. Nie jest, więc bierzemy kolejną liczbe pod divider, nie możemy wziąć kolejnej liczby, ponieważ maksymalna to 3-1, czyli dwa, więc wykonujemy polecenie else. Następnie bierzemy candidate = 4 i divider =2 i sprawdzamy, czy reszta z 4/2 = 0. Jest, więc wykonujemy print i break. Break zatrzymuje pętlę wewnętrzną for (break nie dotyczy if). 
# Itd. jeżeli żaden z warunków w pętli for (wewnętrznej) nie jest spełniony to wykonuje się warunek else. Gdyby nie było break w ifie to else byłoby wykonywane za każdym razem oraz wypisywane byłyby wszystkie dzielniki candidate / divider.


# Przykład 2.
# Dany jest tekst:
# Ten tekst to definicja pewnego pojęcia. Twoim zadaniem jest zbudowanie streszczenia tej definicji poprzez wyświetlenie piewszych 20 słów


text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'


text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'
sepText = text.split(" ")
shortText = ""
count = 0


for word in sepText:
  shortText = shortText + " " + word
  count+=1
  if count >= 20:
	print(shortText)
	break




# Dana jest lista definicji
# Twoim zadaniem jest zbudowanie streszczeń tych definicji poprzez wyświetlenie tylko pierwszych 20 słów z każdej definicji. Zmień w odpowiedni sposób rozwiązanie zadania 1, tak aby przetwarzana była cała lista
definitions = [
   'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
   'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
   'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
   'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.' 
   ]


for definition in definitions:
  shortText = ""
  sepText = definition.split(" ")
  count = 0

  for words in sepText:    
	shortText = shortText + " " + words
	count+=1
	if count >= 20:
  	  print(shortText)
  	  count = 1
  	  break


#  Zadania dodatkowe:

'''1.
Na konto została wpłacona kwota initialCapital w wysokości 20000. Oprocentowanie na koncie to percent = 0.03. Klient banku postanawia oszczędzać przez maxTimeYears = 10 lat. Po każdym roku oszczędzania zarobiona kwota jest dodawana do oszczędności i zarabia odsetki przez pozostały czas.
Zadeklaruj wymagane zmienne, a następnie stwórz pętlę, która wyświetli informację o tym ile pieniędzy jest na koncie pod koniec roku, kiedy odsetki się kapitalizują. Dodaj na zakończenie informację o całkowitej kwocie zarobionej w banku.
'''
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year = 0

while year <= maxTimeYears:
  initialCapital = initialCapital + (initialCapital * percent)
  print(initialCapital)
  year += 1


'''2.
Dana jest liczba całkowita dodatnia number = 20730906, Oblicz sumę cyfr tej liczby.
'''

number = 20730906
result = 0

while number > 1:
  result = number % 10 + result
  number = number // 10
print(result)
  


''' 3. 
dany jest tekst. policz ile jest w nim słów dłuższych od wordLength = 6
'''

tekst = "United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier."

wordList = tekst.split(" ")
#print(wordList)

longWords = 0

for word in wordList:
  if len(word) > 6:
    longWords += 1
  else:
    continue

print(longWords)




''' 4. masz dany text. Twoim zadaniem jest wyświetlić tylko te słowa, które zawierają literkę "p" '''


text = """   Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex, computer graphic-intensive films. Originally, Industrial Light & Magic relied on Unix shell scripting, but it was found that this solution just couldn’t do the job. Python was compared to other languages, such as Tcl and Perl, and chosen because it’s an easier-to-learn language that the organization can implement incrementally. In addition, Python can be embedded within a larger software system as a scripting language, even if the system is written in a language such as C/C++. It turns out that Python can successfully interact with these other languages in situations in which some languages can’t."""

wordsList = text.split(" ")
words = []
for word in wordsList:
  
  if "p" in word:
    words.append(word)
  else:
    continue

print(words)
  


