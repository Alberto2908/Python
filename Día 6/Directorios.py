import os
from pathlib import *

ruta = os.getcwd() #Get Current Work Directory
ruta = os.chdir("F:\\Cursos Udemy\\Python\\Día 6\\carpeta") #Change Directory

archivo = open("Otro_archivo.txt")
print(archivo.read())
#ruta = os.makedirs("F:\\Cursos Udemy\\Python\\Día 6\\carpeta\\otra") #Crear directorio
archivo.close()


ruta2 = "F:\\Cursos Udemy\\Python\\Día 6\\prueba.txt"
elemento = os.path.basename(ruta2)
print(elemento)
elemento = os.path.dirname(ruta2)
print(elemento)
elemento = os.path.split(ruta2)
print(elemento)

#os.rmdir("F:\\Cursos Udemy\\Python\\Día 6\\carpeta\\otra") #Elimina carpeta

otro_archivo = open("F:\\Cursos Udemy\\Python\\Día 6\\carpeta\\Otro_archivo.txt")
print(otro_archivo.read())

carpeta = Path("F:/Cursos Udemy/Python/Día 6/carpeta")
archivo2 = carpeta / "Otro_archivo.txt"

mi_archivo = open(archivo2)
print(mi_archivo.read())
mi_archivo.close()