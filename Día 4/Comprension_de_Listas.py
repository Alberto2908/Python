palabra = "python"

lista1 = []

for letra in palabra:
    lista1.append(letra)

print(lista1)

lista2 = [letra for letra in "python"]
print(lista2)

lista3 = [num for num in range(0,21,2)]
print(lista3)

lista4 = [num/2 for num in range(0,21,2)]
print(lista4)

lista5 = [num for num in range(0,21,2) if num * 2 > 10]
print(lista5)

lista5 = [num if num * 2 > 10 else "no" for num in range(0,21,2) ]
print(lista5)

pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)