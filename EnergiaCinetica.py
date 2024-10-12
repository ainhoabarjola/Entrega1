masa=float(input("Escribe la masa: "))
while (not(masa>1)):
    masa=float(input("La masa no puede ser negativa, pon otra: "))

velocidad=float(input("Escribe la velocidad: "))    
while (not(velocidad>1)):
    velocidad=float(input("La velocidad no puede ser negativa, pon otra: "))  

e=((masa*velocidad**2)/2)
print(f"La Energía Cinética es: {e}")