#21/06/2021
# Anthony Velez
# Software - Tercer semestre


class Cargo:
    secuencia=0
    def __init__(self,des="sin cargo"):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia 
        self.descripcion=des
if __name__ == "__main__":

    cargo1=Cargo ()
    print("cargo",cargo1.codigo,cargo1.descripcion)

    cargo2=Cargo("docente")
    print("cargo",cargo2.codigo,cargo2.descripcion)

    cargo3 = Cargo()
    print("cargo",cargo3.codigo,cargo3.descripcion)
    print(Cargo.secuencia)
