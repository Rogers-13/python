### tuples 

 # deficion
 
my_tuple =tuple()
my_other_tuple=()


my_tuple = (35, 1.77, "rogelio", "olivares","jauregui")
my_other_tuple = (35, 60,30)

print(my_tuple)
print(type(my_tuple))

# acceso a elementos y busqueda

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) #IndexError
#print(my_tuple[-6]) #IndexError


print(my_tuple.count("rogelio"))
print(my_tuple.index("olivares"))
print(my_tuple.index("rogelio"))

# my_tuple[1] = 1.80 'tuple' objetivos does not

 
#contenacion
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# subtuplas
print(my_sum_tuple[3:6])
#tupla mutable con convercion alista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "rogelio"
my_tuple.insert(1,"azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# eliminacion

#del my_tuple [1] #typeErro: tuple objetivos dosen

del my_tuple
print(my_tuple)