placa = int(input("ingrese el ultimo digito de la placa: "))

semana = ["lunes", "martes", "miercoles", "jueves", "viernes"]
 
if placa == 1 or placa == 2:
    print ("tu dia de pico y placa es ", semana[4])
if placa == 3 or placa == 4:
    print ("tu dia de pico y placa es ", semana[0])
if placa == 5 or placa == 6:
    print ("tu dia de pico y placa es ", semana[1])
if placa == 7 or placa == 8:
    print ("tu dia de pico y placa es ", semana[2])
if placa == 9 or placa == 0:
    print ("tu dia de pico y placa es ", semana[3])
else:
    print("ingra un valor valido")
    