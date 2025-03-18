class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color  = color #self.atributo = parámetro
        self.especie = especie

mi_pajaro = Pajaro("Negro", "Tucan")

print(mi_pajaro.color)
print(mi_pajaro.especie)

print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

print(Pajaro.alas)
print(mi_pajaro.alas)