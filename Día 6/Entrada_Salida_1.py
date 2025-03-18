mi_archivo = open("prueba.txt")

#print(mi_archivo.read())
"""una_linea = mi_archivo.readline()
print(una_linea.upper())
una_linea = mi_archivo.readline()
print(una_linea.rstrip())
una_linea = mi_archivo.readline()
print(una_linea)"""

"""for l in mi_archivo:
    print("Aquí dice: " + l)"""

todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)




mi_archivo.close()