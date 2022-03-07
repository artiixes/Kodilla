import sys
import logging

rodzaj = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
p1 = float(input('Podaj pierwszy składnik: '))
p2 = float(input('Podaj drugi składnik: '))
if rodzaj == 1:
    print('Dodaje ' + str(p1) + ' i ' + str(p2))    
    p = p1 + p2
    print('Wynik to ' + str(p))
if rodzaj == 2:
    print('Odejmuje ' + str(p1) + ' i ' + str(p2))
    p = p1 - p2
    print('Wynik to ' + str(p))
if rodzaj == 3:
    print('Mnoże ' + str(p1) + ' i ' + str(p2))
    p = p1 * p2
    print('Wynik to ' + str(p))
if rodzaj == 4:
    print('Dziele ' + str(p1) + ' i ' + str(p2))
    p = p1 / p2
    print('Wynik to ' + str(p))