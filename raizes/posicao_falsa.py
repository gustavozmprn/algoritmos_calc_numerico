import math

#declaração de variáveis
a:float     #extremo a esquerda
b:float     #extremo a direita
c:float     #ponto médio
n:int       #máximo de iterações
TOL:float   #tolerancia

#usando as variáveis
a = -1
b = 1
TOL = 10**-6
n = 15

#função
def f(x:float)->float:
  return math.cos(x) - x           

#####################################################################################################


def posicao_falsa(a, b):
  xp:float
  x0 = a
  x1 = b
  xp = (x0 * f(x1) - x1 * f(x0))/ (f(x1) - f(x0))
  for i in range(2,n,1):
    if abs(min(f(xp),x1-x0) < TOL):
      return [xp, i]
    if (f(x0) * f(xp) > 0):
      x0=xp
    else:
      x1=xp
    xp = (x0 * f(x1) - x1 * f(x0))/(f(x1) - f(x0))
  print(f"Falhou após {n} iterações")
  return 0

print(f'x : {posicao_falsa(a, b)}')