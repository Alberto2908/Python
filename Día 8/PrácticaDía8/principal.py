import numeros

def preguntar():

    print("Bienvenido a Farmacia Python")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmútica")
        try:
            mi_seccion = input("Elija su sección: ").upper()
            ["P", "F", "C"].index(mi_seccion)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador(mi_seccion)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()