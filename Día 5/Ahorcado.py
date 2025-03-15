from random import *

palabras = ["perro","lobo","sopa","fideo","esponja","tractor","coche","camisa","comida","lampara"]
intentos = 6
adivinado = False

def elegir_palabra(lista):
    palabra_elegida = choice(lista)
    return palabra_elegida

def transformar_palabra(palabra):
    palabra_misteriosa = ""
    for l in palabra:
        palabra_misteriosa += "_"
    return palabra_misteriosa

def recibir_letra():
    valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while valida == False:
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in abecedario:
            valida = True
        else:
            print("Letra no válida.")
    return letra_elegida

def comprobar_letra(letra, palabra, vidas):
    lista = []
    for i, l in enumerate(palabra):
        if l == letra:
            lista.append(i)
    if len(lista) == 0:
        vidas-=1
    return lista, vidas

def cambiar_guion(letra, palabra, lista):
    palabra_lista = list(palabra)  # Convertimos la palabra en una lista
    for p in lista:
        palabra_lista[p] = letra  # Modificamos la letra en la posición correcta
    return "".join(palabra_lista)  # Convertimos la lista de vuelta a string

def acertado(palabra, acertado):
    if "_" in palabra:
        acertado = False
    else:
        acertado = True
    return acertado


palabra_elegida = elegir_palabra(palabras)
palabra_final = transformar_palabra(palabra_elegida)

while intentos > 0 and not adivinado:
    print(f"***********\n\n{palabra_final}\n\nTe quedan {intentos} vidas.")
    letra = recibir_letra()
    lista, intentos = comprobar_letra(letra, palabra_elegida, intentos)
    palabra_final = cambiar_guion(letra, palabra_final, lista)
    adivinado = acertado(palabra_final, adivinado)

if acertado:
    print(f"\n🎉 ¡Enhorabuena! Has adivinado la palabra: {palabra_elegida} 🎉")
else:
    print(f"\n💀 Lo siento, has perdido. La palabra era: {palabra_elegida}")