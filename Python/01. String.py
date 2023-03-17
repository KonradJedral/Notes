'''

String
Stringi zapisujemy w “ lub ‘ otwierając i zamykając tekst
text = “To jest text” lub 
text = ‘To jest text’ 
Ważne, że w przypadku gdy chcemy użyć apostrof w tekście to cały tekst bierzemy w cudzysłów
text = “Mc Donald’s”
i na odwrót, gdy chcemy użyć cudzysłowów to zamykamy w apostrofach
text = ‘To jest “cytowany” text’

'''
# 1 zapis
print("Mam 3 braci i 5 sióstr")


# 2 zapis
print("mam {} braci i {} sióstr".format("3", "5"))


# 3 zapis
print("mam {a} braci i {b} sióstr".format(a=3, b=5))


# 4 zapis
a = 3
b = 5
print(f"mam {a} braci i {b} sióstr")
print(f"mam {a:20} braci i {b:20} sióstr")          # rezerwacaja miejsc dla wartości a i b




#5 zapis
print(("Mam %d braci i %s sióstr"%(3, "5")))          # d - decimal (liczba całkowita),   s - string, dlatego w cudzysłowiu


# 6 zapis
family = "mam {a} braci i {b} sióstr".format(a=3, b=5)
print(family)


'''

Podstawowe funkcje:
str.replace(old, new, count) - zmienia starą (old) wartość na nową (new). Opcjonalnie można dodać ile razy ma szukać starych wartości i podmienić na nową (count)
message = "bonjour and welcome to Paris!"
print(message.replace("Paris", "Lyon")) 		 # bonjour and welcome to Lyon!
replaced_message = message.replace("o", "!", 2)
print(replaced_message) 				 # b!nj!ur and welcome to Paris!

str.upper() - zamienia wszystkie litery na duże
str.lower() - zamienia wszystkie litery na małe
print(x.islower())  / print(x.isupper()) - da wartość boolean. Twierdzenie jest prawdziwe lub nie. Przykład wiersza
print(x.upper().isupper()) - zmienna x zostanie zmieniona na duże litery i otrzymamy wartość            				True, ponieważ zmienna x będzie z dużych liter.
str.title() - zamienia pierwsze litery wszystkich słów na duże
str.swapcase() -zamienia małe litery na duże i vice versa 
str.capitalize() - zamienia pierwszą literę w str. na dużą, a resztę na małe
str.lstrip(“string”) - usuwa to co wpisane zamiast “string” od lewej strony. Jeżeli nie będzie nic wpisane to usunie wszystkie spacje od lewej strony
str.rstrip(“string”) - usuwa to co wpisane zamiast “string” od prawej strony. Jeżeli nie będzie nic wpisane to usunie wszystkie spacje od prawej strony 	
str.strip([chars]) -  usuwa to co wpisane zamiast “string” z obydwu stron. Jeżeli nie będzie nic wpisane to usunie wszystkie spacje z obydwu stron
print(len(x)) - długość zmiennej x
print(x[0]) - wyświetli index 0 ze zmiennej x, czyli pierwszą wartość z x, ponieważ indexy liczymy od 0
print(x[3]) - wyświetli intex 3, czyli czwartą wartość z x
x[:3] - wyświetli pierwsze 3 elementy z x
x[3:] - wyświetli wszystkie elementy poza pierwszymi trzema 
print(x.index("y")) - wyświetla który index posiada wartość y w zmienej x. Przykład:
            	x = "Python"
            	print(x.index("t")) - wydrukuje 2, ponieważ P - 0, y - 1, t - 2 itd. UWAGA! rozróżnia małe i duże litery
            	print(x.index("hon")) - wydrukuje 3, ponieważ od tego indexu zaczyna się wartość"hon"
str.casefold() - zamienia na małe litery dodatkowo zmieniając litery obce na takie jak się je czyta np niemieckie B z kreską na “ss”

''' 


# Przykłady:
q = "THE EYES"
print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6]) 
#lub 
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6]) 
# Wyświetli: THEY SEE


q = "a gentleman"
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8:])
# Wyświetli: elegant man




line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(":")+2:]		
#ze zmiennej line dzięki line.find(“:”) wyszukuje pierwszy dwukropek i zwraca jego index, następnie dodaje 2, żeby nie zwracało “:” i spacji i na końcu “:”, żeby wyświetlił wszystko do końca.
print(time)		# wyświetli “22:00”
tmp = line[line.find('"')+1:]
# wyszykuje pierwszy cudzysłów, dodaje 1, żeby go nie wyświetlał i dodaje dwukropek, żeby wyświetlić wszystko do końca
title = tmp[:tmp.find('"')]
#ze zmiennej tmp wybieram wszystko od początku, aż do pierwszego cudzysłowu 
print(title) 		# wynik to - Kropka nad i

print(x.replace("y", "z"))    #   zamienia wartość y na wartość z w zmiennej x 

# Zapis:
str = str.lower() #- prawidłowy
str.lower() #- nieprawidłowy 
# Przykłady:
word = "Mississippi"
print(word.rstrip("ips")) 	 # "M"
#	usunęło wszystkie i, p oraz s od prawej strony, aż trafi na inną literę
print(word.lstrip("ips")) 	# "Mississippi"
#	usunęło wszystkie i, p oraz s od prawej strony, aż trafi na inną literę
print(word.strip("Mips"))  	# ""
#	usunęło wszystkie M,  i, p oraz s od prawej strony, aż trafi na inną literę, czyli całe słowo


# string % value

print('%.3f' % (11/3))  		# 3.667	drukuje do 3 miejsca po przecinku
print('%.2f' % (11/3)) 		 # 3.67		drukuje do 2 miejsca po przecinku


# split
atext = "This is a text"
atext.split(" ")			
#rozdzieli wszystkie elementy oddzielone spacjami i z elementów utworzy tabelę

# str. format() method
# przykład
print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
# Wydrukuje:
# Mix 2 eggs, 30 g of milk and a pinch of salt to make an ideal omelet.

# do {} przypisuje kolejne dane z .format()

# do {} można przypisać nr indexu zmiennych z format(), np:

print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
# Strangers in the Night by Frank Sinatra

print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))
# Night in the Strangers by Frank Sinatra

# można także do {} przypisać nazwy zmiennych z .format(), np:

print('The {film} at {theatre} was {adjective}!'.format(film='Lord of the Rings', adjective='incredible', theatre='BFI IMAX'))

# co wydrukuje: “The Lord of the Rings at BFI IMAX was incredible!”

# można przypisać również w ten sposób:
print('The {0} was {adjective}!'.format('Lord of the Rings', adjective='incredible'))

# natomiast przy takim zapisie będzie błąd:
print('The {0} was {adjective}!'.format(adjective='incredible', 'Lord of the Rings'))


# dzięki .format można również zarezerwować określoną ilość znaków dla danej wartości:
zmienna = "File {0:20s} has size {1:10d} KB"
zmienna.format(file1.txt, 100)
#0 i 1 oznaczają pozycję w .format, 20 i 10  określa ilość zarezerwowanych znaków, natomiast s i d to oznaczenia string i decimal (tekst i liczba całkowita)
# wynikiem 
print(zmienna.format(file1.txt, 100)) 
# będzie:
# File            file1.txt has size        100 KB

# starszy zapis - zamiast .format używamy %
helloMessage = "%s has %d %s"		
#%s - string do wpisania później, %d - liczba do wpisania później

print(helloMessage % ("Chriss", 10000, "$")) 
#znak % a później w nawiasie wartości, które przypisujemy w odpowiedniej kolejności.

# nowy zapis tego samego:
helloMessage2 = "{0} has {1} {2}"

print(helloMessage2.format("Chriss", 10000, "$"))

# Przykład wykorzystania .format z rezerwacją ilości znaków (tworzenie tabeli)
line = "{0:20} cost {1:6} $"
print(line.format("ICE CREAM", 3))
print(line.format("TRIP TO VENICE", 120))
print(line.format("PIZZA HAWAI", 6))
''' wynikiem będzie:
ICE CREAM            costs      3 €
TRIP TO VENICE       costs    119 €
PIZZA HAWAII         costs      6 €
'''

# string z f
print(f"tekst {} w klamrze jakąś zmienną lub funkcje, np {a} lub {b + c} i zamykamy string")

# Inny rodzaj zapisu
# Przykład:
hundred_percent_number = 1823
needed_percent = 16
needed_percent_number = hundred_percent_number * needed_percent / 100

print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
# co wydrukuje:  16% from 1823 is 291.68

print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
# co wydrukuje:  Rounding 291.68 to 1 decimal place is 291.7 - (...number:.1f oznacza podaną wartość do 1 miejsca po przecinku.


# search in string

# in 
# sprawdzamy, czy jakiś string znajduje się (jest częścią) innego stringa, np:
print("apple" in "pineapple") 	 	# True, ponieważ pineapple
print("milk" in "yogurt")      		# False

# startswith / endswith
# Możemy sprawdzić, czy string zaczyna lub kończy się od jakiegoś wyrażenia.
email = "email_address@something.com"
print(email.startswith("www."))          		# False
print(email.endswith("@something.com"))  	# True

# Sprawdzenie, czy dany string zaczyna lub kończy się innym wyrażeniem w danym zakresie: (trzeba pamiętać, że odróżnia wielkie i małe litery) 

# string.startwith(wyrażenie, start, end) -  jeśli będzie tylko jedna dana to określamy od którego indexu ma zacząć sprawdzać 

email = "my_email@something.com"
print(email.startswith("email", 2)) 	# False
print(email.startswith("email", 3))  	# True

email = "my_email@something.com"
print(email.endswith("@", 5, 8))  	# False	- ponieważ w wyszukiwaniu nie bierze udziału 						element z indexem zakończenia 
print(email.endswith("@", 5, 9))  	# True

# index / find
best = "friend"
print(best.find("i"))  	# 2
print(best.index("i"))  	# 2
# Zarówno find jak i index pokazuje który index ma pytane wyrażenie. Różnica jest, że jeżeli find będzie błędny (nie będzie szukanego wyrażenia w stringu) to wyświetli “-1”, natomiast index “ValueError”

print(best.find("end"))  	# 3 - drukuje, od którego indexu zaczyna się “end” w “friend”

# Sprawdzanie w danym obszarze:

string.find(wyrażenie, start, end)    #  index end nie jest częścią wyszukiwania, przykład:
magic = "abracadabra"
print(magic.find("ra", 5))      	# 9  - ponieważ wyszukuje od 5 indexu do końca, ale wynik daje 					z całego stringa magic
print(magic.find("ra", 5, 10))  	# -1 - nie ma “ra” w tym zakresie, ponieważ index 10 nie należy 					do wyszukiwanego obszaru

# rfind / rindex 
# wyszukiwanie od tyłu stringa, np:
magic = "abracadabra"
print(magic.rfind("ra"))  	# 9
print(magic.rindex("a"))  	# 10

# count
# liczenie wyrażeń w stringu
magic = "abracadabra"
print(magic.count("abra"))  	# 2
print(magic.count("a"))     	# 5

# Przykład funkcji z rfind / in 
def check_email(string):
    dot = string.rfind(".")
    mon = string.rfind("@")
if " " in string:
    return False    
elif "@" in string and dot - mon > 1:
    return True
else:
    return False
# Funkcja ta przypisuje do “dot” nr indexu “.”, następnie do “mon” przypisuje nr indexu “@”. Sprawdza, czy w “string” są spacje, jeśli tak to drukuje “False”, jeżeli nie to sprawdza, czy w “string” znajduje się “@”, a następnie, czy jej nr indexu jest mniejszy niż nr indexu “.” i czy nie następują po sobie. Ponieważ kropka musi być po znaku “@” i nie może do niej przylegać. Jeśli się sprawdza to drukuja “True”. W każdym innym przypadku drukuje “False”

# separator 

# sep
print(“USA”, “FR”, “POL”, “BEL”,  sep=”\n”)      
#spowoduje, że każdy parametr zostanie wydrukowany w kolejnej linii

print(“USA”, “FR”, “POL”, “BEL”,  sep=”-”)      
#spowoduje, że każdy parametr zostanie oddzielony minusem (-)

print(“USA”, “FR”, “POL”, “BEL”,  sep=”\t”)      
#spowoduje, że każdy parametr zostanie oddzielony tabulatorem (TAB)


# inne
# \a
print(“This is a bell: \a”) 	# wywołuje domyślny dźwięk systemowy

# Unicode
print(“\u03A3”) 		# wywołuje wartości z Unicodą, które nie są dostępne z klawiatury

# \
print(“This is backslash: \\”) 	# żeby wydrukować \ musimy postawić znak podwójnie


# r format
justText = r”to jest \text z backslashami\!!”
print(justText)		# wydrukuje tak jak jest zapisane w justText pomijając slashe, ponieważ jest “r” przed wartością zmiennej


# Przykład:
quote =  'A good programmer is someone who always looks both ways before crossing a one-way street'

print(quote.upper())	
print(quote.lower())
print(quote.endswith("street"))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find("one"))
print(quote.replace("one", "1"))
print(quote.replace("one", "1").replace("both", "2"))
print(quote.split(" "))
print(quote.isdigit())			
#sprawdza, czy jest liczbą
print(quote.isdecimal())		
#sprawdza, czy może być liczbą dziesiętną (z przecinkiem)
print(quote.isalpha())
#sprawdza, czy są użyte tylko znaki z alfabetu - FALSE ponieważ są spacje
print(quote.isalnum())
# sprawdza, czy są użyte tylko znaki z alfabetu lub numeryczne - też FALSE ponieważ spacja


# Przykład 2 


firstName = 'Kasia'
familyName = 'Sowa'
lastName = 'Mrugala'
newName = firstName+familyName+lastName
print(newName)
# or
newName = firstName+" "+familyName+" "+lastName
print(newName)
music = '"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood'
# or
music = "\"Universal Fanfare\" Jerry Goldsmith \"Happy Together\" Garry Bonner \"I'm a Man\" Steve Winwood"
# wykorzystanie backslasha do zapisu apostrofów lub cudzysłowów w środku stringa
print(music)
music = '"Universal Fanfare" Jerry Goldsmith\n"Happy Together" Garry Bonner\n"I\'m a Man" Steve Winwood\a'
print(music)


print('(\\(\\\n( -.-)\nO_(")(")')
# drukuje coś takiego:
'''
(\(\
( -.-)
O_(")(")

'''


