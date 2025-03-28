from collections import Counter, defaultdict, namedtuple

#Counter
numeros = [8,6,9,5,4,5,5,5,8,7,4,5,4,4]

frase = "al pan pan y al vino vino"

print(Counter(numeros))

print(Counter("mississippi"))

print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,4])
print(serie.most_common())
print(serie.most_common(1))
print(serie.most_common(2))
print(list(serie))

#defaultdict
mi_dic = {"uno":"verde","dos":"azul","tres":"rojo"}
mi_dic2 = defaultdict(lambda : "nada")
mi_dic2["uno"] = "verde"
print(mi_dic2["dos"])
print(mi_dic2)

#namedtuple
mi_tupla = (500, 18, 65)
print(mi_tupla[1])

Persona = namedtuple("Persona", ["nombre","altura","peso"])
ariel = Persona("Ariel",1.76,79)

print(ariel.altura)
print(ariel.peso)
print(ariel[2])