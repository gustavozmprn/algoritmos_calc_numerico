import numpy as np

def pvc_diferencas_finitas(a, b, n, f, alpha, beta):

    h = (b - a) / (n + 1)  # Tamanho do passo
    xs = np.linspace(a, b, n + 2)  # Pontos discretizados (incluindo os contornos)
    
    # Construção do sistema linear
    A = np.zeros((n, n))  # Matriz dos coeficientes
    b_vec = np.zeros(n)   # Vetor dos termos independentes

    for i in range(n):
        x_i = a + (i + 1) * h
        b_vec[i] = f(x_i) * h**2

        if i > 0:
            A[i, i - 1] = 1
        A[i, i] = -2
        if i < n - 1:
            A[i, i + 1] = 1

    # Ajuste para condições de contorno
    b_vec[0] -= alpha
    b_vec[-1] -= beta

    # Resolvendo o sistema linear
    y_interior = np.linalg.solve(A, b_vec)

    # Adicionando os valores dos contornos
    ys = np.concatenate(([alpha], y_interior, [beta]))

    return xs, ys

# Exemplo de uso
f = lambda x: -2  # PVC: y''(x) = -2, com y(0) = 0 e y(1) = 0
a, b = 0, 1
alpha, beta = 0, 0  # Condições de contorno
n = 10  # Número de subdivisões

xs, ys = pvc_diferencas_finitas(a, b, n, f, alpha, beta)
print(f"Valores de x: {xs}")
print(f"Valores de y: {ys}")
