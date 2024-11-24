import math

def lagrange_interpolation(x, y, xp):
    if len(x) != len(y):
        raise ValueError("As listas de x e y devem ter o mesmo tamanho.")

    n = len(x)
    retorno = 0

    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (xp - x[j]) / (x[i] - x[j])
        retorno += L_i * y[i]

    return retorno


x = [2, 3, 4, 5, 6]
y = [4, 6, 8, 10, 12]
xp = 12

result = lagrange_interpolation(x, y, xp)
print(f"O valor interpoaldo para o x = {xp} é y = {result}")