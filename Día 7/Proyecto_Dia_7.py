class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    balance = 0

    def __init__(self, nombre, apellido, numero_cuenta):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNº Cuenta: {self.numero_cuenta}\nBalance: {self.balance}"

    def bienvenida(self):
        print(f"Bienvenido {self.nombre} {self.apellido} a su cuenta {self.numero_cuenta}\n")

    def depositar(self):
        try:
            cantidad = float(input("Cuánto desea ingresar?: "))
            if cantidad > 0:
                self.balance += cantidad
                print(f"\nHas depositado {cantidad}€\n")
            else:
                print("La cantidad debe ser mayor a 0.\n")
        except ValueError:
            print("Error: Introduce un número válido.\n")

    def retirar(self):
        try:
            cantidad = float(input("Cuánto desea retirar?: "))
            while cantidad > self.balance:
                print("Estas intentando retirar más cantidad de la que dispones.")
                cantidad = float(input("Introduce una cantidad válida: "))
            self.balance -= cantidad
            print(f"\nHas retirado {cantidad}€.\n")
        except ValueError:
            print("Error: Introduce un número válido.\n")

    def saldo_actual(self):
        print(f"Saldo actual: {self.balance} €\n")


def crear_cliente(nombre, apellido, numero_cuenta):
    mi_cliente = Cliente(nombre, apellido, numero_cuenta)
    return mi_cliente

def inicio():
    nombre = input("Cuál es tu nombre?: ")
    apellido = input("Cuál es tu apellido?: ")
    numero_cuenta = input("Cuál es tu número de cuenta?: ")
    mi_cliente = crear_cliente(nombre, apellido, numero_cuenta)

    mi_cliente.bienvenida()

    while True:
        mi_cliente.saldo_actual()
        orden = int(input("Qué función desea realizar?:\n\t1) Depositar dinero\n\t2) Retirar dinero\n\t3) Salir\n\t===>"))
        match orden:
            case 1:
                mi_cliente.depositar()
            case 2:
                mi_cliente.retirar()
            case 3:
                print("Gracias por usar nuestro servicio. ¡Hasta pronto!")
                break
            case _:
                print("No existe esa opción. Inténtalo de nuevo")

inicio()