archivo = open("prueba1.txt", "w")
archivo2 = open("prueba.txt", "a")

archivo2.write("\nbienvenido")

archivo.write("hola\n")
archivo.write("mundo\n")

archivo.write("""hola
mundo
aqui
estoy\n""")

archivo.writelines(["hola","mundo","aqui","estoy"])

lista = ["hola","mundo","aqui","estoy"]
for p in lista:
    archivo.writelines(p + "\n")

archivo.close()
archivo2.close()