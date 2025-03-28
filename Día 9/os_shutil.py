import os
import shutil
import send2trash

print(os.getcwd())

archivo = open("curso.txt", "w")
archivo.write("texto de prueba")
archivo.close()

shutil.move("curso.txt", "C:\\Users\\alber\\Desktop")

send2trash.send2trash("C:\\Users\\alber\\Desktop\\curso.txt")

print(os.walk("C:\\Users\\alber\\Desktop"))

ruta = "C:\\Users\\alber\\Desktop"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son: ")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")