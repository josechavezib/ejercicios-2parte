lado_1 = int(input("ingresa el valor del lado 1: "))
lado_2 = int(input("ingresa el valor del lado 2: "))
lado_3 = int(input("ingresa el valor del lado 3: "))

p = (lado_1 + lado_2 + lado_3)/2

a = (p * (p - lado_1) * (p - lado_2) * (p - lado_3)) ** 0.5

#ar= a ** 0.5
print("el area del triuangulo es : ", a)
#print(ar)
