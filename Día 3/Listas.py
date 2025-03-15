mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
otra_lista = ['hola', 55, 6.1]

print(type(mi_lista))
resultado = len(mi_lista)
print(resultado)

resultado = mi_lista[0:]
print(resultado)
print(mi_lista3)

mi_lista3[0] = 'alfa'
print(mi_lista3)

mi_lista3.append('g')
print(mi_lista3)

eliminado = mi_lista3.pop(0) #Elimina el indice que pasas como parámetro. Sin parámetro elimina el último
print(mi_lista3)
print(eliminado)

lista = ['g','o','b','m','c']
lista.sort() #Ordena alfabéticamente
print(lista)

lista.reverse() #Ordena al reves
print(lista)