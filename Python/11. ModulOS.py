# Moduł OS 

import os
import time
"""
os.getcwd()                # zwraca ścieżkę bieżącego katalogu
os.path.join(ścieżka dostępu do katalogu, nazwa pliku)       # tworzy ścieżkę dostępu dla pliku
os.path.abspath(nazwa pliku)  - zwraca bezwzględną ścieżkę dostępu do pliku (bezwzględna- z nazwa dysku, wszystkimi folderami i nazwą pliku)
os.path.basename(ścieżka pliku(składnia r'scieżka')) - zwraca tylko samą nazwę pliku
os.path.dirname(ścieżka pliku(składnia r'scieżka')) - zwraca tylko ścieżkę dostępu do katalogu, gdzie znajduje się plik, bez nazwy pliku
os.path.exists(ścieżka pliku(składnia r'scieżka')) - sprawdza, czy taka ścieżka istnieje
Funkcje dla istniejącego pliku:


os.path.getmtime(ścieżka pliku(składnia r'scieżka')) - sprawdza datę ostatniej modyfikacji - używamy time.localtime
os.path.getctime(ścieżka pliku(składnia r'scieżka')) - sprawdza datę utworzenia - używamy time.localtime
os.path.getatime(ścieżka pliku(składnia r'scieżka')) - sprawdza datę ostatniego dostępu - używamy time.localtime
os.path.getsize(ścieżka pliku(składnia r'scieżka')) - zwraca wielkość pliku w bajtach
os.path.isfile(ścieżka pliku) - sprawdza, czy ścieżka definiuje plik
os.path.isdir(ścieżka pliku) - sprawdza, czy ścieżka definiuje katalog
os.path.split(ścieżka dostępu)[i] - oddziela ostatni element ścieżki, i = [numer elementu, który chcemy oddzielić licząc od końca]
os.path.plitdrive(ścieżka dostępu) - zwraca tuple, w której elementami będą nazwa dysku i pozostała część ścieżki
"""


print("Current directory is: ", os.getcwd())        # zwraca ścieżkę bieżącego katalogu




#budowanie ścieżki dostępu dla stworzonego pliku "results.txt"
currentDir = os.getcwd()
filename = "results.txt"
fullpath = os.path.join(currentDir, filename)      
print("\nThe constructed tile path is: ", fullpath)    


#stworzenie pliku "output.txt" i znalezienie jego bezwzględnej ścieżki dostępu
relativePath = "output.txt"
print("\nThe absolute path is: ", os.path.abspath(relativePath))


# wyodrębnienie ścieżki do folderu gdzie się znajduje plik i samej nazwy pliku:
filepath = r'C:\Programowanie\Projekty\Szkolenie Udemy\geom.py'
print("\nThe fine name part is: ", os.path.basename(filepath))
print("\nThe directory part is: ", os.path.dirname(filepath))


# sprawdzanie, czy ścieżka istnieje:
print("\nIs file existing? ", os.path.exists(filepath))


# sprawdzanie ostatniej modyfikacji, daty utworzenia:
print("The last modify date is: ", time.localtime(os.path.getmtime(filepath)))
print("The create date is: ", time.localtime(os.path.getctime(filepath)))


# wyodrębnienie nazwy pliku innym sposobem:
print("Faile name is: ", os.path.split(filepath)[1])


# Przykład

import os
import time


dir = input("Wprowadz ścieżkę dostępu do katalogu. ")


if os.path.exists(dir) == False:
    print("wskazana ścieżka nie istnieje")
else:
    file = input("Podaj nazwę pliku. ")
    path = os.path.join(dir, file)
    if os.path.exists(path) == False:
        print("wskazany plik nie istnieje")
    else:
        print("Dane pliku: %s " % (path))
        print("The last modify date is: ", time.localtime(os.path.getmtime(path)))
        print("Size in bytes: ", os.path.getsize(path))
        print("Current dir is: ", os.getcwd())
        print("File directory is: ", os.path.abspath(path))




# Sprawdzanie w pętli while, czy podany przez użytkownika plik istnieje.  


import os


while True:
    filename = input("Enter path to file: ")
    if os.path.isfile(filename):
        break
    else:
        print("File name is not correcy, try again!")


print("The results file is %s" % (filename))

