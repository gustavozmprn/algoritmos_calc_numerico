def metodo_runge_kutta_2(f, x0, y0, x_end, h):
    x = x0
    y = y0
    xs = [x]
    ys = [y]

    while x < x_end:
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y += 0.5 * (k1 + k2)
        x += h
        xs.append(x)
        ys.append(y)

    return xs, ys

f = lambda x, y: x - y  # EDO: y'(x) = x - y
x0, y0 = 0, 1  # Condição inicial
x_end = 2
h = 0.1

xs, ys = metodo_runge_kutta_2(f, x0, y0, x_end, h)
print(f"Valores de x: {xs}")
print(f"Valores de y: {ys}")
