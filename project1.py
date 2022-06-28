# 1. Dla liczb od 0 do 10 pokaż 3 kolejne litery od "a" zwiekszonego o licznik pętli
import string

lista = list(string.ascii_lowercase)

print("zadanie 1")
for x in range(0, 10):
     liczba = 0 + x
     print(lista[0 + liczba], lista[1 + liczba], lista[2 + liczba])


#2. To samo, ale dla parzystych pokaż duże litery a dla 5 i 10 wypisz je potrójnie (aaa zamiast a)

print("zadanie 2")

for x in range(0, 11):
     liczba = x
     if x % 2 != 0 and x != 5:
         print(lista[0 + liczba], lista[1 + liczba], lista[2 + liczba])
     elif x == 5:
         print(lista[0 + liczba] * 3, lista[1 + liczba] * 3, lista[2 + liczba] * 3)
     elif x == 10:
         print(lista[0 + liczba].upper() * 3, lista[1 + liczba].upper() * 3, lista[2 + liczba].upper() * 3)
     elif x % 2 == 0 and x != 10:
         print(lista[0 + liczba].upper(), lista[1 + liczba].upper(), lista[2 + liczba].upper())


