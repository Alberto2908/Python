mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

mi_set = set([1,2,3,4,5,1,1,1,1,2,2,2,])
print(mi_set) #Descarta los 1 y 2 repetidos

mi_set = set([1,2,3,4,(1,2,3),5,1,1,1,1,2,2,2,]) #Solo acepta tuples dentro, no acepta listas ni diccionarios
print(mi_set)

mi_set = set([1,2,3,4,5])
print(len((mi_set)))
print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4) #Lo añade porque no existe
print(s1)

s1.add(2) #No lo añade porque ya existe
print(s1)

s1.remove(3) #Elimina ese elemento. Si pongo uno que no existe, da error
print(s1)

s1.discard(6) #Descarta ese elemento. Si no existe, no da error
print(s1)

sorteo = s1.pop() #Elimina un elemento aleatorio
print(sorteo)

s1.clear() #Vacia el set
print(s1)