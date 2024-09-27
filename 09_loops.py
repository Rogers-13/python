#loops#
#while
""""
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # es opcional
    print("mi condicional es mayor o igual que 10")

print("la ejecucion continua")


while my_condition < 20:
    my_condition += 1 
    if my_condition == 15:
        print("se detine la ejecucion")
        break
    print(my_condition)
    
print("la ejecucion continua")
"""
# for
my_list = [35,24,62,52,30,30,17]

for element in my_list :
    print(element)

my_tuple = (35,1.77,"brais","moure","brasis")

for element in my_tuple:
    print(element)   
    
my_set = {"brais", "moure",35}

for element in my_set:
    print(element)
    
my_dict ={"nombre":"bris", "apellido":"moure","edad":35,1:"python"}

for element in my_dict:
    print(element)
    if element == "apellido":
     break


else:
    print("el bucle for para direccion ha finalizado")
    
print("la ejecucion continua")

for element in my_dict:
    print(element)
    if element == "edad":
        continue
    print("se ejecuta")
else:
    print("el bucle for para diccionario ha finalizado")