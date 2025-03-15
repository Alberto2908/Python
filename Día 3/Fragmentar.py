texto = "ABCDEFGHIJKLM"

fragmento = texto[2:5] #fragmenta desde el 2 hasta el 4
print(fragmento)

fragmento = texto[2:] #fragmenta desde el 2 hasta el final
print(fragmento)

fragmento = texto[:5] #fragmenta desde el principio hasta el 4
print(fragmento)

fragmento = texto[2:10:2] #fragmenta desde el 2 hasta el 9, cada 2 caracteres
print(fragmento)

fragmento = texto[::3] #fragmenta cada 3 caracteres
print(fragmento)

fragmento = texto[::-1] #Obtenemos la cadena al revés
print(fragmento)

fragmento = texto[::-2] #Obtenemos la cadena al revés cada 2 caracteres
print(fragmento)