palabra =input("Escribe una palabra: ")

vocales = "aeiouAEIOU" #Al poner las "" no lo identifica como variable sino como cadena de texto

contador = 0

for letra in palabra: #in verifica si un elemento está presente en una secuencia, cadena de texto, conjunto, lista, etc
    if letra in vocales:
        contador += 1

print(f"La palabra tiene, {contador} vocales")