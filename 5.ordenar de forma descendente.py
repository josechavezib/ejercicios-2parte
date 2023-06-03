num_uno = int(input("ingresa el primer numero: "))
num_dos = int(input("ingresa el segundo numero: "))
num_tres = int(input("ingresa el tercer numero: "))


if num_uno > num_dos and num_uno > num_tres:
    if num_dos > num_tres:
        print("el orden descendente es: ", num_uno,",", num_dos, "y ", num_tres)
    else:
        num_tres > num_dos
        print("el orden descendente es: ", num_uno,",", num_tres, "y ", num_dos)         
if num_tres > num_uno and num_tres > num_dos:
    if num_uno > num_dos:
        print("el orden descendente es: ", num_tres,",", num_uno, "y ", num_dos)
    else:
        num_dos > num_uno
        print("el orden descendente es: ", num_tres,",", num_dos, "y ", num_uno)    
if num_dos > num_uno and num_dos > num_tres:
    if num_uno > num_tres:
        print("el orden descendente es: ", num_dos,",", num_uno, "y ", num_tres)
    else:
        num_tres > num_uno
        print("el orden descendente es: ", num_dos,",", num_tres, "y ", num_uno)   
    
if num_uno == num_dos and num_dos == num_tres:
    print(num_uno, ",", num_dos, "y ", num_tres, "son iguales")