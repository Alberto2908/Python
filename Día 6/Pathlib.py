from pathlib import Path, PureWindowsPath

carpeta = Path("F:/Cursos Udemy/Python/Día 6/prueba.txt")

ruta_windows = PureWindowsPath(carpeta)

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")

print(ruta_windows)