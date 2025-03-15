mi_texto = "Esta es una prueba"

resultado = mi_texto[0]
print(resultado)
resultado = mi_texto[9]
print(resultado)
resultado = mi_texto[-4]
print(resultado)
resultado = mi_texto.index("n")
print(resultado)
resultado = mi_texto.index("prueba")
print(resultado)
resultado = mi_texto.index("a") #Solo encuentra una a
print(resultado)
resultado = mi_texto.index("a",5) #Empieza en la posición 5
print(resultado)
resultado = mi_texto.index("a",5, 11) #Empieza en la posición 5 y termina en la 10
print(resultado)
resultado = mi_texto.rindex("a") #Busca de dcha a izq pero devuelve con el indice de izq a dcha
print(resultado)