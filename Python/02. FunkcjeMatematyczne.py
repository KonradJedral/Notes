'''
Matematyka 


int - wartość całkowita
float - ułamek dziesiętny 
abs - wartość bezwzględna (zawsze dodatnia)	#abs(x)
round - zaokrąglanie 				round(x, 2) 		do drugiego miejsca po przecinku
min - najmniejsza wartość
max - największa wartość				max(x, y ,z) - wybierze najmniejsza z podanych wartości 
sum - suma elementów
len - ilość elementów w np. liście

w pythonie nie ma funkcji, która odpowiada za wartość średnią (jest tylko w dodatkowych bibliotekach), dlatego, żeby wyliczyć wartość średnią listy używamy
x = (sum(list)/len(list))

'''

# W przypadku zmiany liczby float na int liczba nie jest zaokrąglana, tylko to co po przecinku jest zwyczajnie ucinane 

x = 3.85  
int(x) = 3     	# nie 4 bo nie zaokrągla



# przykład

percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292, 2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248, 3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169, 4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705, 8.740978348, 6.174819567]
     
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia', 'Norway', 'Portugal','United Kingdom', 'Serbia', 'Germany','Albania', 'France','Czech Republic', 'Denmark', 'Australia', 'Finland', 'Bulgaria', 'Moldova', 'Sweden', 'Hungary', 'Israel', 'Netherlands', 'Ireland', 'Cyprus', 'Italy']

sumOfPoints = 4988


#wyznacz min i max z listy percent

print(min(percent), max(percent))

"""
# Stwórz pętlę for, która wykona się dla zmiennej sterującej i między 0 a (długość listy countries minus 1) Każdorazowo wyświetl:

    odpowiednią wartość z listy percent

    wartość percent "zrzutowaną" na typ int

    wartość percent zaokrągloną do dwóch miejsc po przecinku

    ilość punktów przyznaną danemu krajowi. Da się to obliczyć, bo znamy procentową ilość punktów przyznanych danemu krajowi oraz sumaryczną ilość punktów. Rzutując wynik na int, otrzymasz go w postaci liczby całkowitej

    nazwę kraju
"""

x = 0
for i in countries:
  print(i, "\t", percent[x], "\t", int(percent[x]), "\t", round(percent[x], 2), "\t", int(sumOfPoints*percent[x]/100))
  x += 1




# może również być:

for i in range(len(countries)):
 
    print(percent[i], int(percent[i]), round(percent[i],2), int(round(percent[i]*sumOfPoints/100,0)), countries[i])



