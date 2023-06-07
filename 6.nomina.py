nombre= input("ingrese su nombre: ")
horas = int(input("ingrese horas trabajadas: "))
tarifa = float(input("ingrese la tarifa: "))

sueldoneto= 0
i = 0

if horas<=35:
 sueldoneto = horas * tarifa
elif horas>35:
    sueldoneto = 35 * tarifa + (horas-35) * (tarifa*1.5)
#print (sueldoneto)

sueldo_mensual = sueldoneto * 4

if sueldo_mensual <= 2000:
    i= float(sueldo_mensual) - 0
elif sueldo_mensual > 2000 and sueldo_mensual >= 2220:
    i= float(sueldo_mensual) * 0.80
elif sueldo_mensual > 2220:
    i= float(sueldo_mensual) * 0.70

print (sueldo_mensual)   
print (sueldoneto)
print (i)
    


