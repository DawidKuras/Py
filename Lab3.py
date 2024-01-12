# # #zad 1
# #
# # listaImion = ["Tomasz","Marek","Jan","Arek"]
# # #ver1
# # posortowanalista = sorted(listaImion)
# # print(listaImion)
# # print(posortowanalista)
# #
# # #ver2
# #
# # posortowanalista2 = listaImion.sort()
# #
# # #b)
# #
# # posortowanalista.append("Staszek")
# # posortowanalista.append("Zosia")
# # print(posortowanalista)
# #
# # ostanieImie = posortowanalista.pop()
# # #print(ostanieImie)
# # #print(posortowanalista)
# #
# # #c)
# #
# # posortowanalista.insert(3,"Radek")
# # #print(posortowanalista)
# #
# # posortowanalista.reverse()
# # print(posortowanalista * 2)
#
#
# #zad 2
# #
# # tekst = "Rzeszów jest piekny"
# # print(tekst[1])
# # print(tekst[7])
# # print(tekst[10])
# # print(tekst[13])
# # print(tekst[2])
#
# #zad 3
# #
# # teskt = "Python jest super"
# # print(teskt[0])
# # print(teskt[-1])
# #
# # print(teskt[1:8:2])
# # print(teskt[10::])
# # print(teskt[: :-1])
#
#
# #zad 4
# #a
# # name = str(input("Podaj imię "))
# # print("Witaj", name)
#
# #b
# # age = input("Podaj wiek ")
# # print("Twoj wiek to: ", age)
#
# #c
# # name = str(input("Podaj imie"))
# # surname = str(input("Podaj nazwisko"))
# # lista = []
# # lista.append(name)
# # lista.append(surname)
# # print(name[0],surname[0])
#
# #d
# #
# # chain = input("wpisz losowe wyrazy: ")
# # chain5 = chain * 5
# # print(chain5)
#
#
#
# # zad slowniki
#
# listaZakupow = {"Czekolada" : 18, "Stek" : 70, "Hugo spritz" : 20}
# print(listaZakupow)
# suma = sum(listaZakupow.values())
# print(suma)
#
# #zad 3
#
# rachunki = {"wrzesien": 50, "pazdzernik": 65, "listopad": 57, "grudzien": 72}
# print(rachunki)
# print(sum(rachunki.values()))
# print(max(rachunki.values()))
# print(min(rachunki.values()))
#
# avg = sum(rachunki.values()) / len(rachunki)
#
# #jak wyciagnac ostatnia wartosc**********
# klucze = list(rachunki.keys())
# print(klucze[1])
#
# ostatni = rachunki["grudzien"]
# #print(ostatni)
#
# if ostatni > avg:
#     print("zacznij oszczedzac")
# else:
#     print("jestes bezpieczny")
#
#
#
# zad 4

import random

a = random.randint(3, 7)
b = random.randint(3, 7)

X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

# a
print(f"Zbiór X zawiera liczbę 5: {5 in X}")

# b
print(f"Zbiór X jest podzbiorem zbioru Y: {X.issubset(Y)}")

# c
print(f"Zbiór Y jest podzbiorem zbioru X: {Y.issubset(X)}")

# d
print(f"Zbiór X jest nadzbiorem zbioru Y: {X.issuperset(Y)}")

# e
print(f"Zbiór Y jest nadzbiorem zbioru X: {Y.issuperset(X)}")

# f
print(f"Suma zbiorów X i Y: {X.union(Y)}")

#
print(f"Różnica zbiorów X i Y: {X.difference(Y)}")

# h
print(f"Różnica zbiorów Y i X: {Y.difference(X)}")

# i
print(f"Iloczyn zbiorów X i Y: {X.intersection(Y)}")

# j
print(f"Różnica symetryczna zbiorów X i Y: {X.symmetric_difference(Y)}")

# k
max_value_X = max(X) if X else None
max_value_Y = max(Y) if Y else None
print(f"Najwyższy element w zbiorze X: {max_value_X}")
print(f"Najwyższy element w zbiorze Y: {max_value_Y}")

# l
if X:
    first_element_X = X.pop()
    Y.add(first_element_X)

# m
Y.update(X)

# n
X.clear()
Y.clear()

