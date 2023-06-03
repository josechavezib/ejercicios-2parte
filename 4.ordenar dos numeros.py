num_uno = int(input("ingresa el primer numero: "))
num_dos = int(input("ingresa el segundo numero: "))
orden = ""
if num_uno > num_dos:
    print("el orden ascendente es: ", num_dos, "y ", num_uno)
if num_dos > num_uno:
    print("el orden ascendente es: ", num_uno, "y ", num_dos)
if num_uno == num_dos:
    print(num_uno, " y ", num_dos, "son iguales")