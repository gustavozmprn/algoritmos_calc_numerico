def pvi_diferencas_finitas(f, x0, y0, x_end, h):

    n = int((x_end - x0) / h)  # Número de pontos
    xs = [x0 + i * h for i in range(n + 1)]  # Pontos em x
    ys = [0] * (n + 1)  # Inicialização de y
    ys[0] = y0  # Condição inicial

    for i in range(n):
        ys[i + 1] = ys[i] + h * f(xs[i], ys[i])  # Diferenças finitas para y'

    return xs, ys

# Exemplo de uso
f = lambda x, y: x - y  # EDO: y'(x) = x - y
x0, y0 = 0, 1  # Condição inicial
x_end = 2
h = 0.1

xs, ys = pvi_diferencas_finitas(f, x0, y0, x_end, h)
print(f"Valores de x: {xs}")
print(f"Valores de y: {ys}")
