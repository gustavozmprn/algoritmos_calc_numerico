import math

a:float     #extremo a esquerda
b:float     #extremo a direita
c:float     #ponto médio
n:int       #máximo de iterações
TOL:float   #tolerancia

a = 1
b = 2
TOL = 10**-6

n = 150

#função
def f(x:float)->float:
  return x**3 - x - 2

def bisseccao(a, b):
  for i in range(n):
    c = (a + b) /2
    if (f(c) == 0 or (b - a)/2 < TOL):
      return [c, i]
    if (f(c) * f(a) > 0):
      a = c
    else:
      b = c
  print(f"Não encontrado com {n} iterações")
  return 0
  
print(f'bisseccao: {bisseccao(a, b)}')