### Lists ###
#Definicion

my_list = list()
my_other_list = []

#print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

#print(my_list)
#print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]
'''
#print(type(my_list))
#print(type(my_other_list))

#Acceso a elementos y busqueda
print(my_other_list[0]) #Primer caracter 0
print(my_other_list[1]) #Caracter 1
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
#print(my_other_list[4])#IndexError
#print(my_other_list[-5])#IndexError


print(my_other_list.index("Brais"))
print(my_list.index(30))

age, height, name, lastname = my_other_list
print(name)

name, height, age, lastname, = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

#Concatenacion

print(my_list + my_other_list)
'''
#Creacion, insercion, actualizacion y eliminacion

my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

print( "++++++++++++++++++++++++++++++ operacion con lista ++++++++++++++++++++++++++++++++++++")
#operaciones  con listas 

my_new_list = my_list.copy()


my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# sublitas
print(my_new_list[1:3])

#cambio de tipo
my_list = "Hola paython"
print(my_list)
print(type(my_list))
