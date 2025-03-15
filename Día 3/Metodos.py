texto = "Este es el texto de Alberto"

#Para hacerlo mayúscula
resultado = texto.upper()
print(resultado)

#Para hacerlo minúscula
resultado = texto.lower()
print(resultado)

#Separa por espacios y lo mete en una lista
resultado = texto.split()
print(resultado)

#Separa por letra t y lo mete en una lista
resultado = texto.split("t")
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) #Une elementos de una lista con el caracter de e entre ellos
f = "-".join([a,b,c,d]) #Une elementos de una lista con el caracter de f entre ellos
print(e)
print(f)

#Busca un caracter en mi string. Esto no da error, si no lo encuentra, devuelve -1
resultado = texto.find("g")
print(resultado)

#Reemplaza el texto
resutaldo = texto.replace("e", "x")
print(resutaldo)