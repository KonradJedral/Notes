# Budowa funkcji

def nazwaFunkcji():
    #opis funkcji w komentarzu
    #zawartość funkcji np:
    print("to jest nowa funkcja o nazwie 'nazwaFunkcji'")
    return


# budowanie funkcji z parametrami


def nazwaFunkcji(parametry, funkcji):       #np (year, month, day)
    #opis funkcji w komentarzu
    #zawartość funkcji np:
    print("to jest nowa funkcja, która wyświetli ", parametry, "oraz", funkcji, "jako dwie zmienne, które można przypisać podczas wywoływania funkcji")
    return


# Jeżeli chcemy, żeby naszą funkcję można było wykorzystać to do parametru możemy podać domyślą wartość podczas tworzenia funkcji.




def GiveWorkingDay(year, month=1, day=1):           # przypisujemy domyślne wartości, które będą wykorzystane jeżeli podczas wywoływania
    #wyświetla najbliższy dzień tygodnia                    funkcji nie zostaną przypisane argumenty
    from datetime import date
    from datetime import timedelta
   
   #zawartość funkcji


GiveWorkingDay(2022)        # jeżeli nie podajemy miesiąca i dnia to zostaną wzięte wartości podane jako domyślne, czyli 1 miesiąc i 1 dzień


# możemy też przyjąć jako wartości domyślne bieżący rok, miesiąc i dzień, ale wtedy musimy mieć pewność, że moduł datetime zostanie zaimportowany gdzieś wcześniej w skrypcie


from datetime import date
from datetime import timedelta


def GiveWorkingDay(year=date.today().year, month=date.today().month, day=date.today().day):          
    #wyświetla najbliższy pracujący dzień tygodnia                    
   
  # zawartosć funkcji


# GiveWorkingDay()    # wydrukuje najbliższy pracujący dzień tygodnia patrząc od dzisiaj


# return w funkcji
# W funkcji nie musi być zawarty print. Dzięki return na końcu funkcji określamy co chcemy aby funkcja zwracała
# wynik funkcji jest zwracany pod zmienną nazwy funkcji


def GiveWorkingDay(year=date.today().year, month=date.today().month, day=date.today().day):
    # zawartość funkcji
    return workingday


print(GiveWorkingDay)      
# dzieki takiemu zapisowi wartość workingday z ciała funkcji zostaje przypisana do funkcji GiveWorkingDay
# i możemy ją wykorzystać w dalszej części kodu. Reasumując dostajemy zmienną, którą możemy wykorzystać, zamiast wydrukowanej wartości, tak jak przy użyciu print






# Funkcje ze zmienną ilością parametrów:


def doAction(action, parameter):
    print("action:", action)
    print("parameter:", parameter)
    return


doAction("buy", "shoes")                # pod parametry aciotn i parameter przypisuje podane wartości przy wywoływaniu  i drukuje zawartość funkcji
print("\n")


# Funkcje ze zmienną ilością parametrów: tupla


def doAction2(action, *parameter):          # "*" przed parameter oznacza, że do parameter można dodać kilka elementów, które stworzą tuple
    print("action:", action)
    print("parameter:", parameter)
    for element in parameter:               # dla każdego elementu w parameter zostanie wydrukowany element - element
        print("elements - ", element)
    return


doAction2("buy", "shoes", "socks")          # wydrukuje tak jak w ciele funkcji. 1. acition, 2. parameter (jako tuple), 3. pętle for dla tupli
doAction2("buy", "shoes", "socks", "t-shirt")
print("\n")


# Funkcje ze zmienną ilością parametrów: słownik


def doAction3(action, what, **parameter):       # "**" przed parameter oznacza, że w parameter będzie tworzony słownik
    print("action:", action)
    print("what:", what)
    print("parameter:", parameter)
    for element in parameter:                   # pętla for dla słownika, która wypisuje wszystkie elementy słownika
        print(element, "=", parameter[element]) # element to klucz, a parameter[element] to wartość klucza ze słownika parameter
    return
doAction3("buy", "shoes", size = 45, color = "brown", type = "sport")  
# drukuje tak jak w funkcji. 1. action: buy, 2. what: shoes, 3. cały słownik {"size": 45, "color": "brown", "type": "sport"},
# 4. pętla for dla elementów słownika (size = 45, color = brown, type = sport)






# Wywoływanie funkcji

def nazwaFunkcji():
    #opis funkcji w komentarzu
    #zawartość funkcji np:
    print("to jest nowa funkcja o nazwie 'nazwaFunkcji'")
    return


nazwaFunkcji()          # wydrukowane zosatnie "to jest nowa funkcja o nazwie 'nazwaFunkcji'"


# wywołanie funkcji z parametrami


def nazwaFunkcji(parametry, funkcji):       #np (year, month, day)
    #opis funkcji w komentarzu
    #zawartość funkcji np:
    print("to jest nowa funkcja, która wyświetli ", parametry, "oraz", funkcji, "jako dwie zmienne, które można przypisać podczas wywoływania funkcji")
    return


# nazwaFunkcji(wartość parametru 1, wartość parametru 2)       


# Przykłady

# Budujemy funkcję, która pokaże nam najbliższy pracujący dzień tygodnia:






def GiveWorkingDay():
    #wyświetla najbliższy pracujący dzień tygodnia
    from datetime import date
    from datetime import timedelta


    day = date.today()              # day = dzisiejsza data
    # day = date(2022,10,15)        # do day przypisze podaną date


    if day.weekday() == 5:
        workingday = day + timedelta(days = 2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days = 1)
    else:
        workingday = day


    print("working day for", day, "is", workingday)
    return


# GiveWorkingDay()


# Przykład funkcji z wykorzystaniem parametrów funkcji:


def GiveWorkingDay(year, month, day):
    #wyświetla najbliższy dzień tygodnia
    from datetime import date
    from datetime import timedelta
   
    day = date(year, month, day)        # do day przypisze podaną date


    if day.weekday() == 5:
        workingday = day + timedelta(days = 2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days = 1)
    else:
        workingday = day


    print("working day for", day, "is", workingday)
    return


GiveWorkingDay(2022, 10, 15)        # musisz wpisywać w kolejności takiej jak podana przy definiowaniu funkcji
# GiveWorkingDay(day = 6, month = 12, year = 2022)      #można wywołać w innej kolejności, ale trzeba przypisać wartość do konkretnego parametru


# Jeżeli chcemy, żeby naszą funkcję można było wykorzystać to do parametru możemy podać domyślną wartość podczas tworzenia funkcji.


def GiveWorkingDay(year, month=1, day=1):           # przypisujemy domyślne wartości, które będą wykorzystane jeżeli podczas wywoływania
    #wyświetla najbliższy pracujący dzień tygodnia                    funkcji nie zostaną przypisane argumenty
    from datetime import date
    from datetime import timedelta


   
    day = date(year, month, day)        # do day przypisze podaną date


    if day.weekday() == 5:
        workingday = day + timedelta(days = 2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days = 1)
    else:
        workingday = day


    print("working day for", day, "is", workingday)
    return


GiveWorkingDay(2022)        # jeżeli nie podajemy miesiąca i dnia to zostaną wzięte wartości podane jako domyślne, czyli 1 miesiąc i 1 dzień


# możemy też przyjąć jako wartości domyślne bieżący rok, miesiąc i dzień, ale wtedy musimy mieć pewność, że moduł datetime zostanie zaimportowany gdzieś wcześniej w skrypcie


from datetime import date
from datetime import timedelta


def GiveWorkingDay(year=date.today().year, month=date.today().month, day=date.today().day):          
    #wyświetla najbliższy pracujący dzień tygodnia                      
    day = date(year, month, day)        # do day przypisze podaną podczas wywoływania date


    if day.weekday() == 5:
        workingday = day + timedelta(days = 2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days = 1)
    else:
        workingday = day


    print("working day for", day, "is", workingday)
    return


GiveWorkingDay()
  






# Zmienne ilości parametrów: tupla




from datetime import date


def daysToNewYear(*dates):
   
    for todayDate in dates:
       
        NewYearDay = date(todayDate.year +1 ,1,1)       #jako NewYearDay przyjmujemy wartość date(YYYY, MM, DD), ale rok pobieramy z todayDate, czyli daty podanej przy wywoływaniu
        daysToNewYear = NewYearDay - todayDate
        print("dla daty", todayDate, "do sylwestra zostało ", daysToNewYear.days, "dni")
   
    return


daysToNewYear(date(1995,11,11))
daysToNewYear(date(1999,1,15),date(2000,1,15),date(2019,1,15))




# zmienna ilość parametrów w funkcji (tupla)


def printAnimal(*animals):
    txtBat = r'''
          /\                 /\
         / \'._   (\_/)   _.'/ \
        /_.''._'--('.')--'_.''._\
        | \_ / `;=/ " \=;` \ _/ |
         \/ `\__|`\___/`|__/`  \/
                 \(/|\)/       '''
    txtBear = r'''
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''
    txtCat = r'''
        |\---/|
        | o_o |
         \_^_/'''
    for animal in animals:
        if animal == 'cat':
            print(txtCat)
        elif animal == 'bear':
            print(txtBear)
        elif animal == 'bat':
            print(txtBat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
       
   
    return


print(printAnimal("dog", "bear", "cat", "mice"))
print(printAnimal())



