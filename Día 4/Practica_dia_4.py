from random import *

numero = randint(1,100)
adivinado = False
intento = 0
nombre = input("Cuál es tu nombre?")

print(f"Bienvenido {nombre}, he pensado un número aleatorio entre el número 1 y 100. Tienes 8 intentos para adivinar")
while intento < 8:
    num = int(input(f"Cuál es el número?"))
    intento += 1

    if num < 0 or num > 100:
        print("El número que has dicho es menor que 0 o mayor que 100, no sirve")
    elif num > numero:
        print(f"El {num} es mayor que el número que yo he pensado.")
    elif num < numero:
        print(f"El {num} es menor que el número que yo he pensado.")
    elif num == numero:
            print(f"BIEN!!! Has acertado!!! El número {num} era el que yo había pensado. Has adivinado en {intento} intentos")
            break

if intento == 8:
    print(f"Lo siento, se han agotado los intentos. El número secreto era {numero}")

