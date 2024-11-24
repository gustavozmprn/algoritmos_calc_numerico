import math

#declaração de variáveis
a:float    #aproximação inicial
n:int       #máximo de iterações
TOL:float   #tolerancia

#usando as variáveis
a = 10
TOL = 10**-6
n = 100

#declaração da função
f = lambda x : (x**3) - (10*x**2) - 400      
df = lambda x : (3*x**2) - (20*x)  

#####################################################################################################

def newton(p0):
  for i in range(n):
    p:float
    p = p0 - f(p0)/df(p0)
    if abs(p - p0) < TOL or f(p) < TOL or abs(p-p0)/abs(p) < TOL:
      return [p,i]
    p0 = p
  print(f"O método falhou após {n} iterações")
  return 0

print(newton(a))