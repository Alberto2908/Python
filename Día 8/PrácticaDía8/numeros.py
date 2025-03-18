def decorador(seccion):
    print("\n" + "*" * 23)
    print("Su número es:")
    if seccion == "P":
        print(next(p))
    elif seccion == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será atendido")
    print("*" * 23 + "\n")

def numero_perfumería():
    for n in range(1,100):
        yield f"P-{n}"

def numero_farmacia():
    for n in range(1, 100):
        yield f"F-{n}"

def numero_cosmetica():
    for n in range(1,100):
        yield f"C-{n}"

p = numero_perfumería()
f = numero_farmacia()
c = numero_cosmetica()