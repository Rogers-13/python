### exception handling ###


numeberOne = 5
numeberTwo = 1
#numeberTwo = "1" # se pude aser que esun estrin todo entre comillas 

# excepcion base try except #
""" 
try:
    print(numeberOne + numeberTwo)
    print("no se ha producido un erro")
except:
    #se ejecua si se produce una excepcion
    print("se ha producido un error")
    
    
# flujo completo de una excecpcion : try except el se final
numeberTwo = "a"
try:
    print(numeberOne + numeberTwo)
    print("no se ha producido un error")
except:
    print("se ha producido un error")
else: #opcinal
    # se ejecutara si no produce una excepcion
    print("la ejecucion continua corretamente")
finally:# opcinal
    # SE EJECUTA siempre
    print("la ejecucion continua")

#excepciones por  tipo
numeberTwo = 0

try:
    print(numeberOne + numeberTwo )
    print("no se ha producido error")
except ValueError:
    print("se ha producido un valueError")
except TypeError:
    print("no se ha producido typeerror")
    """
    
    
# captura de la infromacion de excepcion


numeberTwo = "a"
try: 
    print(numeberOne + numeberTwo)
    print("no se ha producido un error")

except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)



    