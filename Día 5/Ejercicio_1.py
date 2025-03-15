def devolver_distintos(n1,n2,n3):
    suma = n1+n2+n3
    """lista = []
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)"""
    lista= [n1,n2,n3]
    lista.sort()
    #menor = lista[0]
    #medio = lista[1]
    #mayor = lista[2]

    if suma > 15:
        #return mayor
        return max(lista)
    elif suma < 10:
        #return menor
        return min(lista)
    elif suma >= 10 or suma <= 15:
        #return medio
        return lista[1]

