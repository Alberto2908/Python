class Pajaro:

    alas = True

    #Métodos de instancia
    def __init__(self, color, especie):
        self.color  = color #self.atributo = parámetro
        self.especie = especie

    def piar(self):
        print(f"Pio pio")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    #Métodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        #Desde aquí podemos acceder a atributos, pero no a parámetros
        cls.alas = False
        print(Pajaro.alas)

    #Métodos estáticos
    @staticmethod
    def mirar():
        print("El pajaro mira")

#Métodos de instancia
piolin = Pajaro("amarillo","canario")
piolin.pintar_negro()
piolin.volar(50)
piolin.alas = False
print(piolin.alas)

#Métodos de clase
Pajaro.poner_huevos(3)

#Métodos estáticos
Pajaro.mirar()