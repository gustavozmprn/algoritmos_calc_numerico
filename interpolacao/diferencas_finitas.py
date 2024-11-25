import math

def gregory_newton(vx, vy, x):
    h = vx[1] - vx[0]
    z = x - vx[0]
    n = len(vx)
    d = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        d[i][0] = vy[i]
    c = n-1
    for j in range(1, n):
        for i in range(0, c):
            d[i][j] = d[i+1][j-1] - d[i][j-1]
        c-=1
    pn = vy[0]
    for i in range(1,n):
        pi = (d[0][i] / math.factorial(i)) * z
        for j in range(1, i):
            pi *= z - j
        pn += pi
    return pn

# Exemplo de uso
x_values = [8, 12, 16, 20]
y_values = [18, 23, 26, 21]
new_x = 17

result = gregory_newton(x_values, y_values, new_x)
print(f"Para x = {new_x}, o valor aproximado de y é: {result}")