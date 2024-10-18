# class ##
# definicion

class MyEmtyPerson:
    pass # para poder dejar la clase vacia



print(MyEmtyPerson)
print(MyEmtyPerson())


# class con construtores , funciones y propirdades privads y publicas

class Person:
    def __init__(self, name, lastname, alias="sin alias"):
        self.full_name = f"{name}{lastname} ({alias})"
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def walk(self):
        print(f"{self.full_name} esta caminado")
        
my_Person = Person ("rogelio", "olivares") 

print(my_Person.full_name)
print(my_Person.get_name())
my_Person.walk()
    
my_other_Person = Person ("rogelio", "olivares", "rogeliodev") # type: ignore
print(my_other_Person.full_name)
my_other_Person.walk()
my_other_Person.full_name = "hector de leon ( el loco de los perros)"
print(my_other_Person.full_name)
    
my_other_Person.full_name = 666
print(my_other_Person.full_name)