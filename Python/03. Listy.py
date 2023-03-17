'''
Listy
listy zapisujemy w nawiasach kwadratowych []

'''
# Żeby wydrukować listę w stringu:

# print(" ".join(nazwaListy))			# “ “ - separator elementów listy w tym przypadku spacja. następnie funkcja join i nazwa listy
# Dodawanie do listy:

# append
# nazwa_listy.append('co dodajemy') - 
# append dodaje jako pojedynczy element na koniec listy (jeśli przez append dodamy inną listę to stworzymy listę zagnieżdżoną) 

# extend
numbers = [1, 2, 3, 4, 5]
numbers.extend([10, 20, 30])	-
# dodaje całą listę jako elementy listy
print(numbers)  	# [1, 2, 3, 4, 5, 10, 20, 30]

# dodawanie
numbers_to_four = [0, 1, 2, 3, 4]
numbers_from_five = [5, 6, 7, 8, 9]
numbers = numbers_to_four + numbers_from_five 
print(numbers) 	 # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# mnożenie elementów w liście
pattern = ['a', 'b', 'c']
patterns = pattern * 3
print(patterns) 		 # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

# insert
list.insert(position, element)	# dodaje element w miejsce gdzie wskażemy (index, element)
years = [2016, 2018, 2019]
years.insert(1, 2017)           # [2016, 2017, 2018, 2019]
years.insert(0, 2015)           # [2015, 2016, 2017, 2018, 2019]
years.insert(len(years), 2020)  # [2015, 2016, 2017, 2018, 2019, 2020]

# podmiana elementu
countries = [‘FR’, ‘US’, ‘DE’, ‘RU’]
countries[1]=’GB’		
# podmieni element o indexie 1 (czyli US) na GB

# podwójne nawiasy
lista[::-1] # odwraca listę
lista[::2] # drukuje co drugi element


# sortowanie 
nazwaListy.sort()     		#sortuje listę według alfabetu
nazwaListy.reverse() 		#odwraca listę

# kopiowanie listy

newList = nazwaListy.copy()
#tworzy nową listę o nazwię newList, która jest kopią nazwaListy

# Usuwanie elementów z listy:

# remove
dragons = [‘Targiss’, ‘'Rudror', 'Coporth']
dragons.remove('Targiss')	- usuwa element z listy (string)
print(dragons)  	# ['Rudror', 'Coporth']
# remove po indexie 
dragons.remove(dragons[1])

# del
dragons = ['Rudror', 'Targiss', 'Coporth']
del dragons[1]		- usuwa element z listy (po indexie)
print(dragons) 		 # ['Rudror', 'Coporth']

# pop
dragons = ['Rudror', 'Targiss', 'Coporth']
last_dragon = dragons.pop()		- wyciąga ostatni element do osobnej listy print(last_dragon) 	 # 'Coporth'		
print(dragons)     	 # ['Rudror', 'Targiss']

# funkcja pop wyciąga element z listy, użyta z print wydrukuje ten wyciągnięty element
print(dragons.pop(1))  	#wyciągnie i wydrukuje element z indexem 1 

# clear
nazwaListy.clear()
# usuwa całą zawartość listy

# Sprawdzanie elementów w liście:

# in / not in  
# zwraca wartość True/False

catalog = ['yogurt', 'apples', 'oranges', 'bananas', 'milk', 'cheese']
 
print('bananas' in catalog)      # True
 
product = 'lemon'
print(product in catalog)        	# False
print(product not in catalog)    # True

# count
# ilość powtórzeń danego elementu w liście
grades = [10, 5, 7, 9, 5, 10, 9]
print(grades.count(5))  	# 2 	- zwraca ile razy 5 pojawia się w liście grades

# szukanie po indexie
grades = [10, 5, 7, 9, 5, 10, 9]
print(grades.index(7)) 		 
 # 2	- wypisuje który nr indexu ma podany w (x) element
print(grades.index(10))	  # 0

# po indexie można szukać również od końca, wtedy zaczynamy liczyć od 1, a nie od zera:
print(grades.index(-2))  	   #0

list.index(element, start, end)		
# wypisuje, który nr indexu(w całej liście) ma element, przeszukując w danym przedziale(bez indexu podanego jako koniec). Jeśli nie ma podanego końca, to szuka do końca listy
grades = [10, 5, 7, 9, 5, 10, 9]
print(grades.index(9, 2, 5))  	# 3
print(grades.index(10, 1))    	# 5


# Sum, min, max, 

cargo = [40, 25, 84, 10, 12, 24, 26, 37, 5]
sum(cargo) - suma elementów w cargo
min(cargo) - najmniejszy element
max(cargo) - największy element




# Ćwiczenie:

hitsTitles = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEAVEN', 'RIDERS ON THE STORM', 'WISH YOU WERE HERE']

hitsTitles.append('CHILD IN TIME')	#dodajemy na koniec listy
hitsTitles.append('AGAIN')
hitsTitles.insert(2, 'HOTEL CALIFORNIA')	#dodajemy w miejsce z indexem 2
hitsTitles.insert(0, 'THE SOUND OF SILENCE')

print(hitsTitles.index('HOTEL CALIFORNIA')) # szukamy indexu HOTEL CAL…

hitsTitles.remove('HOTEL CALIFORNIA')      # odpowiedź “3”

hitsTitles[0] = ('ENJOY THE SILENCE')		
# zmieniamy element w indexie 0 na nowy ('ENJOY THE SILENCE')
print(hitsTitles)

hitsToRead = hitsTitles.copy()		
#tworzymy kopie hitsTitles o nazwie hitsToRead 
hitsToRead.reverse()	
#odwracamy kolejność listy

print(hitsToRead)

hitsToRead.sort()
#sortujemy alfabetycznie

print(hitsToRead)

hitsToRead.pop(0)		#usuwamy element z indexem 0
hitsToRead.pop(0)

print(hitsToRead)

additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']

hitsToRead = hitsToRead + additionalSongs	#dodajemy listy do siebie
# inny zapis hitsToRead.extend(additionalSongs)	


print(hitsToRead)

hitsToRead.remove(hitsToRead[2])	#usuwamy element z indexem 2

print(hitsToRead)

print(hitsToRead.count('WISH YOU WERE HERE'))	#liczymy ilość wystąpień
print(hitsToRead.count('RIDERS ON THE STORM'))
hitsToRead.clear()			#czyścimy listę
print(hitsToRead)
# Inny przykład ze zmianą na tuple na końcu


marketing = ["loyality program", "client promotion", "market research"]
marketing.append("public relations")
print(marketing[2])
marketing.insert(1, "investor relations")


print(marketing)


emailMarketing = marketing.copy()
emailMarketing.sort()
print(emailMarketing)


internalEmails = ["internal communication"]
emailMarketing.extend(internalEmails)
print(emailMarketing)


emailTuple = tuple(emailMarketing)
print(emailTuple)



