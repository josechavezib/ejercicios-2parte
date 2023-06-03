n= int(input("numero de estuduantes. "))
a= 0
b= 0
c= 0
d= 0

for i in range(n):
    peso=  float(input("ingrese el peso del estudiante: "))
    
    if peso < 40: 
        a = a + 1
    elif peso >= 40 and peso <= 50:
        b = b + 1
    elif peso > 50 and peso < 60:
        c = c + 1
    else:
        d = d + 1
        
total1= (a /n) * 100
total2= (b /n) * 100
total3= (c /n) * 100
total4= (d /n) * 100
print ("menos de 40kg",  total1,"%", "mas de 40kg y menos de 50kg", total2,"%" , "mas de 50kg y menos de 60kg", total3,"%" , "y mas de 60kg", total4,"%")

