# Conversión IMPLICITA
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

# Conversión EXPLICITA
numero1 = 5.8
print(numero1)
print(type(numero1))

numero2 = int(numero1)
print(numero2)
print(type(numero2))

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nueva_edad = 1 + edad
print(nueva_edad)