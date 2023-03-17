# Input

# Dane od użytkownika pobieramy za pomocą funkcji input()


# wszystko co podane w input jest stringiem, żeby otrzymać int trzeba specjalnie wskazać wartości, że jest intem.
#inputStr = input()
#inputInt = int(inputStr)




# sprawdzenie, czy podana wartość jest liczbą i działanie na podanej wartości:


while True:
    fileSizeStr = input("Enter the max file size (MB): ")       #pobieramy wartość od użytkownika


    if fileSizeStr.isdecimal():                                 # sprawdzamy, czy podana wartość jest liczbą całkowitą (czy np. nie jest napisane five zamiast 5)
        fileSizeInt = int(fileSizeStr)                          # jeśli jest liczbą całkowitą to konwertujemy do int
        break                                                   # i zamykamy pętlę
                                                                # jeżeli wartość nie będzie liczbą całkowitą to pętla wykona się ponownie, aż nie otrzyma wartości całkowitej
print("The max size is %d MB" % (fileSizeInt))
print("Size in KB is %d" % (fileSizeInt*1024))






# Przykład

# wyliczanie miejsc zerowych z równania kwadratowego






def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()




a = input("Wprowadz wartość a: ")
b = input("Wprowadz wartość b: ")
c = input("Wprowadz wartość c: ")


while True:
    if check_int(a) is False:
        print("Watość %s nie jest liczbą całkowitą" % (a))
        break
    elif check_int(b) is False:
        print("Watość %s nie jest liczbą całkowitą" % (b))
        break
    elif check_int(c) is False:
        print("Watość %s nie jest liczbą całkowitą" % (c))
        break
    elif a == 0:
        print("To nie jest równanie kwadratowe")
        break
    else:
        intA = int(a)
        intB = int(b)
        intC = int(c)
        delta = (intB*intB) - 4*intA*intC
        print("delta = ", delta)


        if delta < 0:
            print("Brak miejsc zerowych")
            break
        elif delta == 0:
            x1 = (-intB)/(2*intA)
            print("Jedno miejsce zerowe równe %.2f" % (x1))
            break
        else:
            x1 = (-intB - delta**0.5)/(2*intA)
            x2 = (-intB + delta**0.5)/(2*intA)
            print("Dwa miejsca zerowe:\n x1 = %.2f \n x2 = %.2f" % (x1, x2))
            break




   

