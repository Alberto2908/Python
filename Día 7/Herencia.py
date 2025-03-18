class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

class Mamifero(Animal):
    pass

print(Pajaro.__bases__) #Nos muestra de que clase hereda
print(Animal.__subclasses__()) #Nos muestra a que clases transmite su herencia

piolin = Pajaro(2, "amarillo")
piolin.nacer()
print(piolin.color)