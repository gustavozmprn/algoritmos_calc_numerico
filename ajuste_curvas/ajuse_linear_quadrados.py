import numpy as np
import matplotlib.pyplot as plt


x = np.array([1.0, 3.0, 4.0])  # Valores de x
y = np.array([3.0, 7.0, 9.0])  # Valores de y correspondentes


x_mean = np.mean(x)
y_mean = np.mean(y)
n = len(x)
b1 = (n * np.sum(x*y) - (np.sum(x) * np.sum(y)))/((n * np.sum(x**2)) - (np.sum(x)**2)) # fórmula descrita no pdf
b0 = (np.sum(y) - (b1 * np.sum(x))) / n # fórmula descrita no pdf
x_line = np.linspace(min(x), max(x), 100) # só arrumando um vetor maior, para ficar melhor na hora de plotar
y_line = b1 * x_line + b0 # seguindo a ideia de que o novo y = b0 + b1 * x

plt.scatter(x, y, color='red', label='Dados')
plt.plot(x_line, y_line, color='blue', label=f'Reta ajustada: y = {b1:.2f}x + {b0:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste Linear pelo Método dos Mínimos Quadrados')
plt.grid(True)
plt.show()
