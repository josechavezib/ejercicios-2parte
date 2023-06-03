num_uno = int(input("ingresa el primer numero: "))
num_dos = int(input("ingresa el segundo numero: "))

if num_uno > num_dos:
    print(num_uno, "es mayor")
elif num_dos > num_uno:
    print(num_dos, "es mayor")
elif num_uno == num_dos:
    print(num_uno, " y ", num_dos, "son iguales")
else:
    print("ingresa un valor valido")