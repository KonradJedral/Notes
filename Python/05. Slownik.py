'''

Słownik
klucze

''' 


cars = {
	“brand” : “Toyota”,
	“year” : “2020”,
	“model” : “Yaris”
}

print(cars[“year”]) - wyświetli “2020”
cars[“year”] = 1999
print(“after change”, cars[“year”])

# dodawanie do słownika
cars['is_big'] = ['no', 'yes', 'maybe'] 		#jeśli nie ma w słowniku to się doda
print('Cars after added is_big', cars)



# Przykład lekcji z Udemy:
countryLeaders={“PL”:”Duda”, “US”:”Trump”}
print(countryLeaders[“US”])		#wydrukuje Trump, ponieważ jest to wartość klucza US

# Dodawanie do słownika

countryLeaders[“DE”] = “Merkel”	#w nawiasie kwadratowym klucz, po znaku = wartość

print(countryLeaders)			#{“PL”: “Duda”, “US”: “Trump”, “DE”: “Merkel”}

items()
# wyświetla kolekcję elementów związanych ze sobą w słowniku
print(countryLeaders.items())	
# wyświtli: dict_items([(“PL, “Duda”), (“US”, “Trump”), (“DE”, “Merkel”)])

keys()
# wyświetla klucze zawarte w słowniku
print(countryLeaders.keys())
# wyświetli: dict_keys([“PL”, “US”, “DE”])

values()
# wyświetla wartości zawarte w słowniku
print(countryLeaders.values())
# wyświtli: dict_values([“Duda”, “Trump”, “Merkel”])

pop(klucz)
# wyświetla i usuwa wybrany element 
print(countryLeaders.pop("PL"))
print(countryLeaders)
# wyświetli: 
(“PL”: “Duda”)
{“US”: “Trump”, “DE”: “Merkel”}

popitem()
# zwraca ostatnią wartość ze słownika, a następnie ją usuwa
print(countryLeaders.popitem())
print(countryLeaders)
# wyświetli:
(“DE”: “Merkel”)
{“PL”: “Duda”, “US”: “Trump”}

setdefault(klucz, wartość)
# wyciągamy wartość z podanego klucza, jeżeli nie mamy jeszcze podanego klucza w swoim słowniku to automatycznie zostanie na stałe dodany klucz wraz podaną wartością

print(countryLeaders.setdefault(“FR”, “Macron”))
print(countryLeaders)
# wyświetli:
# Macron 			
# do tej pory nie było klucza FR, dlatego został na stałe dodany wraz z wartością “Macron” oraz wyświetlony
{“PL”: “Duda”, “US”: “Trump”, “DE”: “Merkel”, “FR”, “Macron”}	
#klucz FR i wartość Macron została od razu dodana, więc podczas drukowania całego słownika również została wydrukowana


get(klucz)
# pobiera wartość ze słownika. Jeżeli klucza nie będzie to wyświetli None
print(countryLeaders.get(“PL”)
# wyświeli:
# Duda

update(nowy słownik)
# dodaje nowy słownik do starego, zaznaczając, że jeżeli w nowym słowniku znajduje się taki sam klucz to wartość zostanie podmieniona na nową
newLeaders = {“RU”: “Putin”, “DE”, “Schulz”}
countryLeaders.update(newLeaders)
print(countryLeaders)
# wyświetli:
{“PL”: “Duda”, “US”: “Trump”, “DE”: “Schulz”, “FR”, “Macron”, “RU”, “Putin”}	


# Przykład:

chanels = {"Google": 1480, "Email": 300, "Natural Traffic": 440, "TV Spot": 700}

print(chanels)				#drukujemy cały słownik
print(chanels["Email"])		#drukujemy wartość z klucza Email

chanelsUpdate = {"Natural Traffic": 520, "News": 600}

print(chanelsUpdate)

chanels.update(chanelsUpdate)	
#dodajemy i aktualizujemy klucze i wartości w chanels o słownik chanelsUpdate

print(chanels)
chanels.pop("Email")		#usuwamy klucz Email

print(chanels)


# Przykład:

# Dany masz słownik:
dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less than 50%'} 
'''
Wyświetl zestawienie w postaci (kolejność nie jest istotna):
A - 80%-100%
B - 60%-80%
C - 50-60%
D - less than 50%
'''

for key in dictionary:
  print(key, "-", dictionary.get(key))		
#pobiera key, czyli A, następnie “-” później pobiera(get) wartość przypisaną do key 

