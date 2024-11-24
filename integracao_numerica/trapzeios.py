import math

def metodo_trapezio(f, a, b, n):
    
    h = (b - a) / n  # Tamanho do intervalo
    soma = 0.5 * (f(a) + f(b))  # Contribuição das extremidades

    for i in range(1, n):
        soma += f(a + i * h)

    return soma * h

# Exemplo de uso

f = lambda x: (math.cos(x) + x)/math.pi  # Função a integrar
a, b = 0, 4*math.pi  # Intervalo de integração
n = 3  # Número de subdivisões

resultado = metodo_trapezio(f, a, b, n)
print(f"Integral pelo método do trapézio: {resultado:.10f}")
