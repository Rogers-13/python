'''

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string +" "+ my_other_string)

my_new_line_string = "este es un estring\ncon saltode liea"
print(my_new_line_string)

my_tab_string = "\tEste es un Srting con tabulacion"
print(my_tab_string)

my_scape_string = "\\t Este es un string \\n escapado"
print(my_scape_string)

# formato
name, lastname, age = "rogelio", "olivares", 33
print("Mi nombre es {} {} y mi edad es {}".format(name, lastname ,age))
print("Mi nombre es %s %s y mi edad es %d" % (name, lastname ,age))
print("Mi nombre es " + name + " " + lastname + "y mi eded es" + str(age))
print(f"Mi nombre es {name} {lastname} y mi edad es {age}")
'''


# desempaquetado de caracteres 
languange = "python"
''''
a, b, c, d, e, f =languange
#print(b)
#print(e)


#divicion
languange_slice= languange[1:3]
print(languange_slice)

languange_slice= languange[-2]
print(languange_slice)

languange_slice= languange[0:6:2]
print(languange_slice)

# reverse
reversed_languange = languange [::-1]
print(reversed_languange)
'''
# funcion del lenguajr con cadenas

print(languange.capitalize())
print(languange.upper())
print(languange.count("t"))
print(languange.isnumeric())
print("1".isnumeric())
print(languange.lower())
print(languange.lower ().isupper())
print(languange.startswith("py"))
print("py" == "py") # no es lo mismo