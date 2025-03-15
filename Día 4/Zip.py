nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','México']

combinado = list(zip(nombres,edades))
print(combinado)

combinado2 = list(zip(nombres, edades, ciudades))
print(combinado2)

for nombre,edad,ciudad in combinado2:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")