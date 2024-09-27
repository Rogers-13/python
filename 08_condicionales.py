## condicionales ##
#if
my_condition = True


if my_condition: # es lo mismo que if my_condition == true:
    print("se ejecuta la condicion del if")
    
    my_condition = 5 * 5
    if my_condition == 10:
        print("se ejecuta la condicion del segundo if")


# if, elif, else
if my_condition >10 and my_condition < 20:
    print("es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("es igual a 25")

else:
    print("es menor o igual que 10 o mayor o igual que 20 o distinto 25")
    print("la ejecion continua")
    
# condicionales con ispecion de valor

my_string = ""
my2_string = "Mi micadena de textoooo"



if not my_string:
    print("mi cadena de texto vacia")
    
if my2_string == "Mi micadena de textoooo":
    print(" esta cadenada de texto coincide")  
        
        