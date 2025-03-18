class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("Que tal?")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar() #Dice "Hola" porque primero hereda de padre
print(Nieto.__mro__) #Method Order Resolution. Muestra el orden en el que busca el método
mi_nieto.reir()
