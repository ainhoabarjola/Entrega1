import numpy as np
import matplotlib.pyplot as plt

# Definir coeficientes aleatorios de la función cuadrática
a = 7
b = 3
c = 6

x = np.linspace(-10, 10, 400) # Crea un array de 400 valores que comienzan en -10 y terminan en 10, con cada valor separado uniformemente del siguiente.

# Calcular los valores de y usando la ecuación de la parábola
y = (a*x**2 + b*x + c)

# Graficar la parábola
plt.plot(x, y, label=f'y = {a}x^2 + {b}x + {c}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de la Parábola')
plt.legend() #muestra una leyenda 
plt.grid(True) #activa la cuadrícula en la gráfica
plt.show() # muestra la gráfica en una ventana emergente