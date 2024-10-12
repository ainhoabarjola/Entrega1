n=int(input("Escribe un número entero: "))

while (not(n>1)):
    n=int(input("Ese número no vale, pon otro: "))       

for num in range(1,n+1):
    print(num)
