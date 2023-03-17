
'''
Tuple (Krotki)


tzw. listy statyczne, zapisywane są w zwykłych nawiasach
nazwaTuple = (“element1”, “element2”, “element3”, …)
Tupli nie możemy modyfikować używając funkcji append, extend, remove, pop itd.
Żeby można było zmienić zawartość tupli to musimy zmienić ją na listę 
nazwaNowejListy = list(nazwaTupli)
tak samo z listy można zrobić nową Tuplę
nazwaNowejTupli = tuple(nazwaListy)

'''

# Dostępne działania na tupli to takie, które pozwalają nam wyciągać z nich informacje 

# Tworzenie tupli
tax = (4, 7, 10, 23)

# szukanie po indexie:

print(tax[2])  		#wynik 10
print(tax[-2])		#również wynik 10

# funkcja index 

tax.index(7) 		#szuka na którym miejscu (indexie) znajduje się element “7”
print(tax.index(7))	#wynik 1

# funkcja count

tax.count(8)		#liczy ile razy w tupli występuje wartość 8
print(tax.count(8))	# wynik 1

# max

max(tax)		#szuka najwyżeszej wartości w tupli tax
print(max(tax))		#wynik 23



# Zmiana wartości poprzez tworzenie listy i tupli

tax = (4, 7, 10, 23)
newList = list(tax)		#tworzymy listę o nazwię newList z danymi z tupli tax
newList.append(30)		#dodajemy do listy elementy “30”
newTax = tuple(newList)	#tworzymy nową tuple z nowymi danymi


# Przypisywanie wartości z tupli do zmiennych

(tax1, tax2, tax3, tax4) = tax 
Print(tax1, tax2, tax3, tax4)	# 4 7 8 23
#stworzyliśmy zmienne tax1 do tax4, którym przypisaliśmy wartości z tupli tax

# Zamiana wartości zmiennych 
a = 1 
b = 10

(a, b) = (b, a) 
# W tym przypadku do zmiennej “a” przypisujemy wartość zmiennej “b” i na odwrót, do zmiennej “b” przypisujemy wartość zmiennej “a” 

print(a, b) 		#10 1 		
print(a, "\t"b) 		#10 	1 	#zapis \tb dodaje tabulator przed wartością zmiennej b



