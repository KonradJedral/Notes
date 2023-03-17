'''

Sets 

Tworzenie setów
'''
empty_set = set() # pusty set 

# możemy stworzyć dowolny set, lub pobrać go z listy i wydrukować. 
# Pobrana lista/set zostanie wydrukowany w losowej kolejności z pominięciem powtarzających się elementów.

# Set możemy również zapisać jako “dict” w nawiasach klamrowych, wtedy przy print nie trzeba wpisywać “set”

flowers = {'rose', 'lilac', 'daisy'}
print(flowers)  		# {'daisy', 'lilac', 'rose'}  

# można to też zapisać jako:

flowers = set('rose', 'lilac', 'daisy')  	#  zapisujemy jako set i drukuje set
print(flowers)

# lub

flowers = ('rose', 'lilac', 'daisy')	# zapisujemy jako lista, ale przy printcie zmieniamy na set
print(set(flowers))

# set może zawierać również jedno słowo, np:

letters = set('philharmonic')
print(letters)  # {'h', 'r', 'i', 'c', 'o', 'l', 'a', 'p', 'm', 'n'}

# wtedy drukuje wszystkie litery ze słowa nie powielając powtarzających się liter.

# Dlatego, że set nie powiela tych zamych elementów to sprawdzając długość setu liczy powielany element tylko raz, np

letters = set('Hello')
print(len(letters))  	# the length equals 4 - ponieważ “l” powtarza się dwukrotnie

# Porównywanie dwóch setów nie sprawdza ich kolejności, a zawartość, dlatego:

set1 = {'A', 'B', 'C'}
set2 = {'B', 'C', 'A'}
print(set1 == set2)	  # True

# Dodawanie do setów

# nazwa.add(x) - w celu dodania pojedynczego elementu “x” do setu “nazwa” (niezależnie czy int, czy str)
# nazwa.update(x) - w celu dodania innego setu lub listy “x” do setu “nazwa” 
# Przykłady: 

nums = {1, 2, 2, 3}
nums.add(5)
print(nums) 	# {1, 2, 3, 5}

another_nums = {6, 7}
nums.update(another_nums)
print(nums) 	 # {1, 2, 3, 5, 6, 7}
text = ['how', 'are', 'you']
nums.update(text)
print(nums)  	# {'you', 1, 2, 3, 5, 6, 7, 'are', 'how'}

word = 'hello'
nums.add(word)
print(nums)  	# {1, 2, 3, 'how', 5, 6, 7, 'hello', 'you', 'are'}

# Usuwanie z setów

# nazwa.remove(x)  - usuwa wszystkie elementy “x” z setu “nazwa”
# nazwa.discard(x) - usuwa wszystkie elementy “x” z setu “nazwa”

nums = {1, 2, 2, 3}
nums.remove(3)
print(nums)  		# {1, 3}

# różnica pomiędzy remove, a discard - jeżeli elementu “x” nie będzie w secie “nazwa” to remove wydrukuje “KeyError: x”, natomiast discard wydrukuje”nothing happened”. Przykład:

empty_set = set()
empty_set.discard(2)  	# nothing happened
empty_set.remove(2)  	# KeyError: 2

# nazwa.pop() - usuwa losowy element z setu

nums = {1, 2, 2, 3}
nums.pop()
print(nums)  # {2, 3}

# nazwa.clear() - usuwa wszystkie elementy z setu

# frozenset

# frozenset możemy stworzyć z listy, string’a lub setu, np:

frozenset_from_set = frozenset({1, 2, 3})
print(frozenset_from_set)  		# frozenset({1, 2, 3})

frozenset_from_list = frozenset(['how', 'are', 'you'])
print(frozenset_from_list)  		# frozenset({'you', 'are', 'how'})

# frozenset jest to zwykły set, którego nie możemy zmieniać ( nie można dodawać, ani usuwać nic do setu).
# Możemy natomiast dodać frozenset do innego setu, np:

some_frozenset = frozenset(text)
nested_text.add(some_frozenset)
print(nested_text)  		# {'!', frozenset({'world', 'hello'})}

# Działania na setach

# .union lub “|”, czyli sumowanie setów

# Sumowanie różnych setów można wykonać poprzez funkcję .union lub wstawienie znaku “|” pomiędzy sety, np:

democrats = {'Kennedy', 'Obama'}
republicans = {'Trump', 'Lincoln'}
# operator
presidents = democrats | republicans
# method
also_presidents = democrats.union(republicans)
# let's compare
print(presidents == also_presidents)
# The output is True

# Przy takim dodawaniu setów musimy stworzyć nowy set (presidents i also_presidents), można też dodać jeden set do drugiego nie tworząc nowego setu:

ghostbusters = {'Peter', 'Raymond', 'Egon'}
soldiers = {'Winston'}
secretaries = {'Janine'}

ghostbusters |= soldiers
ghostbusters.update(secretaries)
print(ghostbusters)		# The output is {'Peter', 'Raymond', 'Egon', 'Winston', 'Janine'}

# Wybór wspólnych elementów z setów

# funkcja .intersection lub znak “&”

light_side = {'Obi-Wan', 'Anakin'}
dark_side = {'Palpatine', 'Anakin'}
both_sides = light_side.intersection(dark_side)
print(both_sides)				# The output is {'Anakin'}
print(light_side & dark_side)			# The output is {'Anakin'}

# Wybór wspólnych elementów z dwóch setów 

# funkcja intersection_update lub znak “&=”

creatures = {'human', 'rabbit', 'cat'}
pets = {'rabbit', 'cat'}
creatures.intersection_update(pets)
print(creatures)				# The output is {'rabbit', 'cat'}
# ponieważ z setu “creature” zostały usunięte wszystkie elementy, które nie znajdują się w secie “pets”
beasts = {'crocodile', 'cat'}
creatures &= beasts
print(creatures)				# The output is {'cat'}
# ponieważ z {‘rabbit’, ‘cat’} usunięto poza {‘crocodile’, ‘cat’}, czyli ‘rabbit’ zostaje usunięty i zostaje sam ‘cat’


# Usunięcie wspólnych elementów z setu

# funkcja difference lub znak “-”

painters = {'Klimt', 'Michelangelo', 'Picasso'}
ninja_turtles = {'Michelangelo', 'Leonardo'}
print(painters.difference(ninja_turtles))		# The output is {'Klimt', 'Picasso'}
print(painters - ninja_turtles)			# The output is {'Klimt', 'Picasso'}

# usuwa z pierwszego setu elementy wspólne dla obydwu setów.

# żeby wyrzucić wspólne elementy dwóch setów z pierwszego można też użyć
# difference_update lub “-=”

criminals = {'Al Capone', 'Blackbeard', 'Bonnie and Clyde'}
gangsters = {'Al Capone'}
pirates = {'Blackbeard'}

criminals.difference_update(gangsters)
criminals -= pirates
print(criminals)					# The output is {'Bonnie and Clyde'}


'''!!!!!! przy .union, “|”, .intersection, “&”, .difference, “-” !!!!!!
Tworzy się nowy set, dlatego można zapisać 
set A
set B
set C = set A | set B
 lub bez nazywania 
print(set A | set B)

Natomiast 
!!!!!! .intesection_update, “&=”, .difference_update, “-=” !!!!
usuwa z pierwszego podane setu nie tworząc nowego, czyli najpierw trzeba wykonać działanie, a później wpisać print.
set A 
set B 
setA.intersection_update(setB)
print(set A)

nie można wpisać print(setA.intersection_update(setB))
''' 
# operator *

# w setach możemy użyć operatora * w celu rozpakowania setów w setach

languages = [{'c', 'c++', 'python'}, {'python', 'javascript'}, {'python', 'java'}]
the_best = set.intersection(*languages)
print(the_best)				# The output is {'python'}

# odpowiedź jest ‘python’, ponieważ wspólnym elementem wszystkich zagnieżdżonych setów jest ‘python’



