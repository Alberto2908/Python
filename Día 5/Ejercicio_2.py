def funcion(palabra):
    lista = []
    for letra in palabra:
        if letra not in lista:
            lista.append(letra)
        else:
            pass
    lista.sort()
    return lista

print(funcion("esternocleidomastoideo"))