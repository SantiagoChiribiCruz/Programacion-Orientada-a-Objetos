class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza =raza

    def ladrar(self):
        print(f"{self.nombre} esta ladrando")   
        
nombre = input("Digame el nombre de su perro:")
edad = input("Digame la edad de su perro:")
raza = input("Digame la raza de su perro:")
mi_perro = Perro(nombre, edad, raza)

mi_perro.ladrar()



