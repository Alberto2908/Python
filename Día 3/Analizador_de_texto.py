texto = input("Escribe un texto: ")
texto = texto.lower()
palabras = texto.split()

letras = []
letras.append(input("Escribe una letra: ").lower())
letras.append(input("Escribe otra letra: ").lower())
letras.append(input("Escibe una última letra: ").lower())

cont1 = texto.count(letras[0])
cont2 = texto.count(letras[1])
cont3 = texto.count(letras[2])

#1 Cuantas veces aparece cada letra. Almacenar letras en una lista y usar metodo de string que cuente cuantas veces aparece
print(f"1.\n\tLa letra '{letras[0]}' aparece {cont1} veces.")
print(f"\tLa letra '{letras[1]}' aparece {cont2} veces.")
print(f"\tLa letra '{letras[2]}' aparece {cont3} veces.")

#2 Cuantas palabras hay en total en el texto. Transformar texto en lista y calcular longitud
print(f"2.\n\tEl texto tiene {len(palabras)} palabras.")

#3 primera y última letra. Indexación
print(f"3.\n\tLa primera letra del texto es: {texto[0]}\n\tLa última letra del texto es: {texto[-1]}")

#4 mostrar texto si invertimos el orden de las palabras. Invertir orden de lista y unir elementos con espacios intermedios.
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"4.\n\tEl texto al revés sería el siguiente:\n\t{texto_invertido}")

#5 Aparece python? Booleano para comprobar y diccionario para respuesta
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"5.\n\tEn el texto {dic[buscar_python]} aparece la palabra 'Python'.")
