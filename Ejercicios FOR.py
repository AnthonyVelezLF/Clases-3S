# Anthony Velez
# Software - Tercer semestre


class For:
    def __init__ (self):
        pass
    def usoFor(self):
        #CICLO REPETITIVO DE INCREMENTO O DECREMENTO SE EJECUTA POR VERDADERO
        true=0
        nombre= "Anthony"
        datos=["Anthony",21,true]
        numeros=(2,5.6,4,1)
        docente={'nombre':'Anthony','edad':21,'fac':'faci'}
        listanotas=[(30,40),(20,40),(50,40)]
        listaalumnos=[{"nombre":"Luis","final":70},{"nombre":"Jean","final":60},{"nombre":"Ariel","final":90}]
        j=0
        while j<5:
            print("while",j)
            j=j+1
        print()
        for i in range(5):
            print("for",i,end=" ")
        print()
        for i in range(1,5):
            print("for",i,end=" ")
        print()
        for i in range(2,10,2):
            print("for",i,end=" ")
        print()
        for i in range(12,3,-3):
            print("for",i,end=" ")
        print()
        
        print("_________________________________________")
        lon=len(datos)
        for pos in range(lon):
            print(pos,datos[pos])
        print()
        print("_________________________________________")
        lon=len(numeros)
        for pos in range(lon):
            print(pos,numeros[pos])
        print()
        print("_________________________________________")
        for elem in nombre:
            print(elem,end=" ")
        print()
        print("_________________________________________")
        for pos, valor in enumerate(datos):
            print(pos,valor,end=" ")
        for clave,valor in docente.items():
            print(clave,valor,end=" ")
        print()
        print("_________________________________________")

        for notas in listanotas:
            print("for externo",notas)
            for nota in notas:
                print(nota,end=" ")
            
            print("saliendo del for interno")
        print("_________________________________________")

        for notas in listanotas:
            acum=0
            for nota in notas:
                acum=acum+nota
            print(acum/2,end=" ")
            
        print()
        print("_________________________________________")
        listaalumnos=[{"nombre":"Luis","Final":70},{"nombre":"Jean","Final":60},{"nombre":"Ariel","Final":90}]
        print("\nDiccionario de alumnos")
        print(listaalumnos)
        acum=0
        acum=0
        for alumnos in listaalumnos:
            print(alumnos)
            for clave, valor in alumnos.items():
                print(clave,":",valor,type(valor),end=" ")
                if type(valor)== int:
                    acum=acum+valor
            print()
        print("Promedio",acum/3)
        print()
        print("_________________________________________")
bucle=For()
bucle.usoFor()