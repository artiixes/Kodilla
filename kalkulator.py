import sys
import logging

types = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
p1 = float(input('Podaj pierwszy składnik: '))
p2 = float(input('Podaj drugi składnik: '))

match types:
    case 1:
        print (p1 + p2)
    case 2:
        print (p1 - p2)
    case 3:
        print (p1 * p2)
    case 4:
        print (p1 / p2)
    case _:
        print("Wrong number!!")
