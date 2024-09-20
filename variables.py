

my_string_variable = "My Strring variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_float_variable = 1.8
print(my_float_variable)
print(type(my_float_variable))

my_int_to_str_variable = str (my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = False
print(my_bool_variable)
print(type(my_bool_variable))


my_bool_variable = true
print(my_bool_variable)
print(type(my_bool_variable))

# comentario de la variable
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("este es el valor:",my_bool_variable)

#alunas funciones del sistema
#len obtiene largo de la cadena
print(len(my_string_variable))

#variable en sola linea cuando con abusar de esta sintaxis
name, surname, alias , age = "brais","more",35
print("me llamo:", name, surname,".miedad")
 

# Inpus 
name = input('¿cual es tu nombre?')
age = input('cuantos años tienes ?')
print(name)
print(age)
print(type(name))
print(type(age))


# cambios su tipo 
name = 38
age = "roy"
print(name)
print(age)
print(type(name))
print(type(age))

# ¿formazamos el tipo?
address: int = 1
#address = input('¿cual es tu direccion')
#addres = true
#addres = 5
#addres = 1.5
print(type(address))