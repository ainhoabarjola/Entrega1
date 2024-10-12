n=int(input("Escribe el radio del círculo: "))

while (not(n>1)):
    n=int(input("Ese número no puede ser negativo, pon otro: "))       


num=(3.14*n**2)
print("El área es: " + str(num))