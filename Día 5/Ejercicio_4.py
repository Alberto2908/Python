def contar_primos(numero):
    primos = [2]
    iteraccion = 3

    if numero < 2:
        return 0

    while iteraccion < numero:
        for n in range(3,iteraccion,2):
            if iteraccion % n == 0:
                iteraccion+=2
                break
        else:
            primos.append(iteraccion)
            iteraccion+=2
    print(primos)
    return len(primos)

print(contar_primos(50))