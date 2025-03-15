lista = [1,2,3,4]

for numero in lista:
    print(numero)

#Esto sería igual a esto:

for numero in range(1, 5):
    print(numero)

#Si necesitamos por ejemplo numeros del 1 al 100, no hace falta hacer una lista a mano con numeros 1 a 1
lista = list(range(1, 101))

print(lista)