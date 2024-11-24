import math

def metodo_simpson(f, a, b, n):
    
    if n % 2 != 0:
        raise ValueError("O número de subdivisões (n) deve ser par para o método de Simpson.")

    h = (b - a) / n  # Tamanho do intervalo
    soma = f(a) + f(b)  # Contribuição das extremidades

    # Soma dos termos ímpares
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)

    # Soma dos termos pares
    for i in range(2, n, 2):
        soma += 2 * f(a + i * h)

    return soma * h / 3

# Exemplo de uso
f = lambda x: (math.cos(x) + x)/math.pi # Função a integrar
a, b = 0, 4*math.pi  # Intervalo de integração
n = 6  # Número de subdivisões (deve ser par)

resultado = metodo_simpson(f, a, b, n)
print(f"Integral pelo método de Simpson: {resultado:.10f}")
