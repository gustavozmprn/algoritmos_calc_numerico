import math
import matplotlib.pyplot as plt

TOL:float

TOL = 10**-3

def metodo_trapezio(f, a, b, n):
    x = []
    fx = []

    h = (b - a) / n  # Tamanho do intervalo
    soma = 0.5 * (f(a) + f(b))  # Contribuição das extremidades
    x.append(a)
    fx.append(f(a))
    for i in range(1, n):
        soma += f(a + i * h)
        x.append(a + i * h)
        fx.append(f(a + i * h))
    x.append(b)
    fx.append(f(b))
    return [x, fx, soma * h]

# Exemplo de uso

f = lambda x: (math.e ** (-x **2))  # Função a integrar
a, b = 0, 1  # Intervalo de integração
n = 3  # Número de subdivisões


resultado1 = metodo_trapezio(f, a, b, 2)
resultado2 = metodo_trapezio(f, a, b, 3)
while (resultado2[2] - resultado1[2] > TOL):
    n+=1
    resultado1 = resultado2
    resultado2 = metodo_trapezio(f, a, b, n)
resultado = resultado2

#resultado = metodo_trapezio(f, a, b, n)
print(f"Quantidade de iteracoes: {n}")
print(f"Integral pelo método do trapézio: {resultado[2]:.10f}")


plt.plot(resultado[0], resultado[1], color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Integração numérica através do método do Trapézio')
plt.grid(True)
plt.show()

