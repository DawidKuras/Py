# #zad 1
# wiek = int(input("podaj wiek"))
#
# if wiek < 4:
#     print("wejescie za free")
# elif 4 <= wiek <= 18:
#      print("wejscie za 10zł")
# else:
#     print("wejscie za 20zł")


#zad 2
# litera = input("Wprowadź literę: ")
#
# if litera.isalpha():
#     if litera.isupper():
#         print("Wprowadzona litera jest duża.")
#     elif litera.islower():
#         print("Wprowadzona litera jest mała.")

#zad 3

# x = float(input("Podaj pierwsza liczbe:"))
# y = float(input("Podaj druga liczbe:"))
# z = input("jakigo znaku chcesz uzyc(+,-,*,/,^)")
#
# op= {"+": x+y, "-": x-y, "*": x*y, "/": x/y, "^": pow(x,y) }
#
# if z == "+":
#     print(op["+"])
# elif z == "-":
#     print(op["-"])
# elif z == "*":
#     print(op["*"])
# elif z == "/":
#     print(op["/"])
# elif z == "^":
#     print(op["^"])


#zad 4

# import cmath
#
# a = int(input("Podaj współczynnik a: "))
# b = int(input("Podaj współczynnik b: "))
# c = int(input("Podaj współczynnik c: "))
#
#
# delta = b ** 2 - 4 * a * c
#
# print("delta wynosi: ",delta)
# p_delta = cmath.sqrt(delta)
#
# x1 = (-b + p_delta) / (2 * a)
# x2 = (-b - p_delta) / (2 * a)
#
# if delta < 0:
#     print("Równanie nie ma rozwiązań")
# else:
#     print("Rozwiązania równania kwadratowego:")
#     print("x1 =", x1)
#     print("x2 =", x2)


#zad 5


# x = float(input("Podaj pierwszą liczbę (x): "))
# y = float(input("Podaj drugą liczbę (y): "))
# z = float(input("Podaj trzecią liczbę (z): "))
#
#
# if x > y:
#     x, y = y, x
# if y > z:
#     y, z = z, y
# if x > y:
#     x, y = y, x
#
#
# print("Liczby po posortowaniu:", x, y, z)