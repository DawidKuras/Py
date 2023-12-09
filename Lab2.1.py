#zad1
#
# for i in range(1,101):
#     print(i)
#
# for a in range(7,78,7):
#     print(a)
#
# a = 101
# for q in range(101):
#     a = a - 1
#     print(a)
#
# b = 22
# for q in range(11):
#     b = b - 2
#     print(b)

#zad2
#
# a = int(input("podaj liczbe "))
# for i in range(a):
#     for q in range(a):
#         print("x",end=" ")
#     print("")

#zad3
#
# a = int(input("podaj liczbe: "))
# for i in range(a):
#     for q in range(i+1):
#         print("x",end=" ")
#     print("")
#
#
# n=1
# for i in range(a):
#     print( a* " " +"x"*n)
#     a=a-1
#     n=n+2

#zad4
#
# q = int(input("podaj liczbe n "))
# a = int(input("pierwszy wyraz ciagu "))
# r = int(input("róznica ciagu "))
# w=0
# for i in range(1,q+1):
#     w = a + (i - 1) * r
#     print(w)

#zad5
#
# liczba = int(input("podaj wartosc: "))
# a = 1
# if liczba == 0:
#     print("zero silnia wynosi: 1")
# else:
#     while liczba >= 1:
#         a = a * liczba
#         liczba = liczba - 1
#     print("silnia wynosi: ", a)