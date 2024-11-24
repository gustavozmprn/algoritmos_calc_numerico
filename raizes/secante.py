import math

#declaração de variáveis
a:float     #extremo a esquerda
b:float     #extremo a direita
c:float     #ponto médio
n:int       #máximo de iterações
TOL:float   #tolerancia

#usando as variáveis
a = 20
b = 30
TOL = 10**-6
n = 100

#declaração da função
f = lambda x : (x**3) - (10*x**2) - 400        

#####################################################################################################

def secante(x0:float, x1:float):
  xp:float
  for i in range(n):
    if (f(x1) < TOL):
      return [x1,i]
    xp = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
    x0 = x1
    x1 = xp
  print(f"O método falhou após {n} iterações")
  return 0

print(secante(a,b))
