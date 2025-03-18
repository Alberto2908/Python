from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona","Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")

print(guia)
print(guia2)
print(guia.parent) #Devuelve la carpeta padre
print(guia.parent.parent) #Devuelve la carpeta padre del padre
print(guia.parent.parent.parent)

#Para enumerar todos los archivos .txt del directorio Europa
guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob("*.txt"):
    print(txt)

#Para enumerar todos los archivos .txt del directorio Europa y sus subdirectorios
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

#Lee desde el punto elegido, hasta el final de la ruta
guia = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa = guia.relative_to("Europa")
en_espana = guia.relative_to("Europa","España")
print(en_europa)
print(en_espana)