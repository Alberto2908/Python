mi_tuple = (1,2,3,4)
t = (5, 4.5, 'ff')

print(type(mi_tuple))
print(mi_tuple[2])
print(mi_tuple[-1])

mi_tuple = (1,2,(10,20),4)
print(mi_tuple[2])
print(mi_tuple[2][0])

mi_tuple = list(mi_tuple) #Convertir en lista
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple) #Convertir en tuple
print(type(mi_tuple))

t = (1,2,3)
x,y,z = t #Forma de asignar valores a variables, siempre y cuando haya la misma cantidad de elementos
print(x,y,z)

t = (1,2,3,1)
print(len(t))
print(t.count(1)) #Cuenta las veces que aparece ese valor
print(t.index(2)) #Devuelve en que índice se encuentra ese valor