""" num=20
nombre="Anita"
print(num,type(num))
print(nombre,type(nombre))

def mensaje(msg):
    print(msg)
    
mensaje("Mi primera clase en python")
mensaje("Mi segunda clase en python") """

class Clase2:
    instan=0               #atributo de clase
    def __init__(self,datos="llamando al constructor" ):
        self.frase=datos   #atributo de instancia
        Clase2.instan=Clase2.instan+1 
        
ejercicio1 = Clase2()#instancia clase: se crea un objeto
print("Sintasis del ejercicio 1 es: {}".format(Clase2.instan)) #cuenta las instancias
print(ejercicio1.frase)
"""ejercicio2 = Clase2("hola guapo")
print("Sintasis del ejercicio 2 es: {}".format(Clase2.instan)) #cuenta las instancias
print(ejercicio2.frase)
ejer3 = Clase2("terminado y entendido")
print("Sintasis del ejercicio 3 es: {}".format(Clase2.instan)) #cuenta las instancias
print(ejer3.frase)"""



