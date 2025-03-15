nombre = input("Cuál es tu nombre?: ")
ventas = float(input("Cuánto has vendido este mes?: "))

comision = round(ventas * 13 / 100, 2)

print(f"Hola {nombre}, tus comisiones de este son de {comision}€. Enhorabuena!")