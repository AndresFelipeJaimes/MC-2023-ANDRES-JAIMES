import math
h = 0.005
x = 0.45
def ErrorAbsoluto(ValorActual,ValorAnterior):
  Resultado = abs((ValorActual-ValorAnterior)/ValorActual)*100
  return Resultado
def Taylor ():
  i=0
  Resultado = 0
  while i <= 15:
    ValorAnterior = Resultado
    if i == 0:
      Derivada = (math.e)**-x
    elif i % 2 == 1:
      Derivada = -((math.e)**-x) * (h**i) / math.factorial(i) 
    else:
      Derivada = ((math.e)**-x) * (h**i) / math.factorial(i) 
    Resultado = Derivada + Resultado
    print("ORDEN #", i, "\n")
    print("El valor de la serie de Taylor es de:\n", Resultado)
    print("El valor del error absoluto es de:\n",  ErrorAbsoluto(Resultado,ValorAnterior),"\n")
    ValorAnterior = Derivada
    i = i+1
Taylor()