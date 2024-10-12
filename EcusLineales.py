import numpy as np

a1 = float(input("Ingresa el valor que acompaña a X en la primera ecuación: "))
b1 = float(input("Ingresa el valor que acompaña a Y en la primera ecuación: "))
c1 = float(input("Ingresa el valor de detrás del igual de la primera ecuación: "))
a2 = float(input("Ingresa el valor que acompaña a X en la segunda ecuación: "))
b2 = float(input("Ingresa el valor que acompaña a Y en la segunda ecuación: "))
c2 = float(input("Ingresa el valor de detrás del igual de la segunda ecuación: "))

A = np.array([[a1, b1],
              [a2, b2]]) #define la matriz de coeficientes, [] separa las columnas
B = np.array([c1, c2]) #define el vector de términos independientes
X = np.array(["X","Y"])

print("\nRepresentación matricial del sistema:") #\n pone una linea de espacio entre la frase de arriba y esta
print(f"{A} * {X} = {B}")

sol = np.linalg.solve(A, B) #comando que resuelve un sistema de ecuaciones

print("\nLas soluciones son:")
print(f"[Xo,Yo] = {sol}")