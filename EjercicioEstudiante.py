class Estudiante:
    def __init__(self, Nombre, Edad, Grado):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Grado = Grado

    def Estudiar(self):
        print("Estudiando...")

Nombre = input ("Ingrese su nombre: ")   
Edad = input("Ingrese su edad: ")
Grado = input("Ingrese su grado: ")

estudiante = Estudiante(Nombre, Edad, Grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.Nombre} \n
      Edad: {estudiante.Edad} \n
      Grado: {estudiante.Grado} \n



    """)
print("INGRESE LA PALABRA (ESTUDIAR)")
while True:
    Estudiar = input()
    if (Estudiar.lower() == "estudiar"):
     estudiante.Estudiar()


        