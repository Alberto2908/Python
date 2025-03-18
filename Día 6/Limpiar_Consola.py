from os import system

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system("cls") #"cls" si es windows, "clear" cualquier otro sistema operativo

print(f"Tu nombre es {nombre} y tienes {edad} años")