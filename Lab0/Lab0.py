# #zadnie 3
# a = int(input("Podaj pierwszy bok prostokąta: "))
# print(a)
#
# b = int(input("Podaj drugi bok prostokata: "))
# print(b)
#
# pole = a * b
# obwod = 2 * a + 2 * b
#
# print("pole prostokata: ", pole)
# print("obowd prostokata: ", obwod)
# print("obowd prostokata: "+ str(obwod))

#zadanie 4

# #s = int(input("podaj dlugosc drogi: "))
# import random
# s = random.randint(1, 100000)
# print(s)
#
# spalanie = float(input("Podaj srednie spalanie w litrach na 100km: "))
# print(spalanie)
#
# zuzycie = s / spalanie
# koszt = zuzycie * 6.5
#
# print("spalone paliwo", zuzycie)
# print("koszt przejechanej drogi: ", koszt)


#zadanie dodatkowe 1

# print("Bedziemy teraz liczyc rownienie liniowe :) ")
#
# a = int(input("Podaj wspolczyniik a: "))
# b = int(input("podaj wspolczynnik b: "))
# print("a =",a ,"|", "b =",b)
#
# if a == 0:
#     if b == 0:
#         print('Równanie tożsamościowe')
#     else:
#         print('Równanie sprzeczne')
# else:
#     x = -b/a
#     print('x =', x)

#zadanie dodatkowe 2

# import  math
#
# print("bedziemy liczyc pole trojkta o bokach a, b, c")
#
# a = float(input("podaj a"))
# b = float(input("podaj b"))
# c = float(input("podaj c"))
#
# print("bok a:",a)
# print("bok b:",b)
# print("bok c:",c)
#
# p = (a+b+c)/2
#
# P = math.sqrt(p*(p-a) * (p-b) * (p-c))
# print("Pole trojkota wynosi: ",P)


#zadanie dodatkowe 3
#
# x = float(input("Podaj pierwsza liczbe:"))
# y = float(input("Podaj druga liczbe:"))
# z = input("jakigo zznaku chcesz uzyc(+,-,*,/,)")
#
# op= {"+": x+y, "-": x-y, "*": x*y, "/": x/y}
#
# if z == "+":
#     print(op["+"])
# elif z == "-":
#     print(op["-"])
# elif z == "*":
#     print(op["*"])
# elif z == "/":
#     print(op["/"])


