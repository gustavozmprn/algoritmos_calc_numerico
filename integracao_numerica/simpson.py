import math
import matplotlib.pyplot as plt

TOL:float

TOL = 10**-3

def metodo_simpson(f, a, b, n):
    
    if n % 2 != 0:
        raise ValueError("O número de subdivisões (n) deve ser par para o método de Simpson.")

    h = (b - a) / n  # Tamanho do intervalo
    x_vals = [a + i * h for i in range(n + 1)]  # Pontos x
    fx_vals = [f(x) for x in x_vals]  # Valores de f(x)
    soma = f(a) + f(b)  # Contribuição das extremidades

    # Soma dos termos ímpares
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)

    # Soma dos termos pares
    for i in range(2, n, 2):
        soma += 2 * f(a + i * h)

    return [x_vals, fx_vals, soma * h / 3]

# Exemplo de uso
f = lambda x: (math.e ** (-x **2))  # Função a integrar
a, b = 0, 1  # Intervalo de integração
n = 4  # Número de subdivisões (deve ser par)

resultado1 = metodo_simpson(f, a, b, 2)
resultado2 = metodo_simpson(f, a, b, 4)
while (resultado2[2] - resultado1[2] > TOL):
    n+=2
    resultado1 = resultado2
    resultado2 = metodo_simpson(f, a, b, n)
resultado = resultado2
print(f"Quantidade de iteracoes: {n}")
print(f"Integral pelo método de Simpson: {resultado[2]:.10f}")

plt.plot(resultado[0], resultado[1], color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Integração numérica através do método de Simpson')
plt.grid(True)
plt.show()
