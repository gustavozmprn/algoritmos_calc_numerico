import matplotlib.pyplot as plt
import math
import numpy as np


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

def exact(x:float):
    return x/(1 + np.log(x))

f = lambda x, y: y/x - (y/x)**2
x0, y0 = 0, 1  # Condição inicial
x_end = 2
h = 0.1

#xs, ys = metodo_runge_kutta_2(f, x0, y0, x_end, h)
#print(f"Valores de x: {xs}")
#print(f"Valores de y: {ys}")

t, P = metodo_runge_kutta_2(f, 1, 1, 3, 0.25)
u, Q = metodo_runge_kutta_2(f, 1, 1, 3, 0.1)
v, R = metodo_runge_kutta_2(f, 1, 1, 3, 0.05)

y_values1 = exact(t)
y_values2 = exact(u)
y_values3 = exact(v)

errors_1 = np.abs(y_values1 - P)
errors_2 = np.abs(y_values2 - Q)
errors_3 = np.abs(y_values3 - R)

#plt.plot(v, y_values3, 'green', label='analítico' )

#plt.plot(t, P, 'r', label='h = 0.25')
#plt.plot(u, Q, 'b', label='h = 0.1')
#plt.plot(v, R, 'y', label='h = 0.05')


plt.plot(t, errors_1, 'r', label='erro 0.25', linestyle='dashed')
plt.plot(u, errors_2, 'blue', label='erro 0.1', linestyle='dashed')
plt.plot(v, errors_3, 'yellow', label='erro 0.05', linestyle='dashed')



plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
