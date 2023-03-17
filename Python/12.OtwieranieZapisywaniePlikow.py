# Otwieranie plików

# Otwieranie plików na różne sposoby:


# 1. Pamiętamy o otwarciu i zamknięciu pliku:


file = open("C:\\Programowanie\\Projekty\\Szkolenie Udemy\\modulostest.txt", "r") # 1. ścieżka pliku i podwójnymi \\, 2. sposób czytania pliku r - odczyt
content = file.read()
print(content)
file.close()


# 2. stosowany do małych plików - nie musimy pamiętać o zamykaniu pliku


with open("C:\\Programowanie\\Projekty\\Szkolenie Udemy\\modulostest.txt", "r") as file: # odczyt w zmiennej o nazwie file
    content = file.read()
    print(content)


# lub


with open("C:\\Programowanie\\Projekty\\Szkolenie Udemy\\modulostest.txt", "r") as file:
    for line in file.readlines():       # każdorazowo funkcja readlines() odczytuje cały plik i wybiera tylko kolejną linie
        print(line)




# sposób do dużych plików i najlepszy


with open("C:\\Programowanie\\Projekty\\Szkolenie Udemy\\modulostest.txt", "r") as file:
    for line in file:
        print(line)




# Można jeszcze czytać po ilości bajtów, zamiast linijek


with open("C:\\Programowanie\\Projekty\\Szkolenie Udemy\\modulostest.txt", "r") as file:
    fragment = file.read(10)                #odczytuje pierwsze 10bajtów z pliku
    while fragment:
        print(file.tell(), fragment)        # jeśli jest co odczytać to je drukuje  (funkcja tell mówi w którym miejscu tekstu jesteśmy)
        fragment = file.read(10)            # odczytuje kolejne 10bajtów z pliku i zaczyna pętle jeszcze raz





# Zapisywanie do plików


        # ZAPIS danych do plików




# otwieramy tak jak przy odczycie, ale zamist "r", sposób czytania pliku zaznaczamy na "w" - write, "a" - append lub "w+" - do zapisywania i do oczytu
# Ważne !!! Write za każdym razem usunie zawartość pliku i doda to co chcemy, żeby dodał
    #Append doda zawartość do zawartości, która już tam jest.


# 1 sposób
filename = "C:\\Programowanie\\Projekty\\Szkolenie Udemy\\modulostest.txt"
line = "Europe"


file = open(filename, "w")      # odtworzymy plik modulostest w formie do zapisu pod zmienna file
file.write(line)                # dodajemy do modulostest napis ze zmiennej line, czyli "Europe"


file.close()


# gdy chcemy dodać zawartość listy


filename = "C:\\Programowanie\\Projekty\\Szkolenie Udemy\\modulostest.txt"
cities = ["London", "Berlin", "Paris", "Warsaw", "Madrid", "Rome"]


file = open(filename, "w")
file.writelines(cities)         # taki zapis doda wszystkie elementy z listy cities do pliku ciągiem (bez spacji itp)
file.close()


# Lepszy sposób


filename = "C:\\Programowanie\\Projekty\\Szkolenie Udemy\\modulostest.txt"
cities = ["London", "Berlin", "Paris", "Warsaw", "Madrid", "Rome"]


file = open(filename, "a")          # dopisujemy do już zawartych treści
file.write("\n")                    # dodajemy sobie nową linie, żeby oddzielić od tego dodanego wcześniej
for city in cities:  
    file.write(city+", ")           # po + i w cudzysłowiu zapisujemy czym maja być oddzielone elementy z listy


file.close()


#inny zapis


filename = "C:\\Programowanie\\Projekty\\Szkolenie Udemy\\modulostest.txt"
cities = ["London", "Berlin", "Paris", "Warsaw", "Madrid", "Rome"]


with open(filename, "a") as file:
    file.write("\n")
    for city in cities:
        file.write(city + "\t")


# Przykład Zapisywanie linków

import os




webaddresses = []
line = input("Podaj adres strony: ")


while len(line) > 0:
    webaddresses.append(line)
    line = input("Podaj kolejny adres strony: ")




print(webaddresses)


dirname = os.getcwd()
filename = input("Podaj nazwę pliku, w którym chcesz zapisać adresy www. ")
filepath = os.path.join(dirname, filename + ".txt")


with open(filepath, "w") as file:
    for webadress in webaddresses:
        file.write(webadress + "\n")







# Analiza linków i przypisanie do innych plików 

import os


filename = input("Podaj ścieżke dostępu do pliku. ")


while True:  
    if os.path.isfile(filename):
        break
    else:
        print("Spróbuj ponownie.")
        filename = input("Podaj ścieżke dostępu do pliku. ")
webadresses = []


with open(filename, "r") as file:
    for line in file:
        line = line.replace("\n", "")
        webadresses.append(line)            # lub w jednej linij  webadresses.append(line.replace("\n", ""))




for line in webadresses:
    if line.endswith(".pl"):
        with open(os.getcwd() + "\\websPL.txt", "a") as file:
            file.write(line + "\n")
       
    else:
        with open(os.getcwd() + "\\websOther.txt", "a") as file:
            file.write(line + "\n")
           
print("Process finish")


"""
zamiast:
for line in webadresses:
    if line.endswith(".pl"):
        with open(os.getcwd() + "\\websPL.txt", "a") as file:
            file.write(line + "\n")
       
    else:
        with open(os.getcwd() + "\\websOther.txt", "a") as file:
            file.write(line + "\n")
jeśli używamy innej lokalizacji niż aktualnej to:


dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname,'websPl.txt')                # ścieżka do pliku websPL
websPathOther = os.path.join(dirname,'websOther.txt')           #ścieżka do pliku websOther
for line in webadresses:
    if line.endswith(".pl"):
        with open(websPathPL, "a") as file:
            file.write(line + "\n")
       
    else:
        with open(websPathOther, "a") as file:
            file.write(line + "\n")










"""

