X = 0.5
H = 0.1
def Ecuacion (x):
  Resultado = 0.25*x**4 - 0.35*x**2 + 2.5
  return Resultado
def Ecuacion1 (x):
  Resultado = x**3 - 0.7*x
  return Resultado
def Ecuacion2 (x):
  Resultado = 3*x**2 - 0.7
  return Resultado
def Delante (x,y):
  Resultado = (x-y)/H
  return Resultado
def Atras (x,y):
  Resultado = (x-y)/H
  return Resultado
def Centrada (x,y):
  Resultado = (x-y)/(2*H)
  return Resultado
def Delante2 (x,y,z):
  Resultado = (x-y+z)/H**2
  return Resultado
def Atras2 (x,y,z):
  Resultado = (x-y+z)/H**2
  return Resultado
def Centrada2 (x,y,z):
  Resultado = (x-y+z)/H**2
  return Resultado
  
print("El valor verdadero de la primera derivada son:\n", Ecuacion1(X))
print("El valor de F(X + H) es:\n", Ecuacion(X+H))
print("El valor de F(X - H) es:\n", Ecuacion(X-H))
print("El valor de la primera diferencia finita dividida hacia adelante es:\n", Delante(Ecuacion(X+H), Ecuacion(X)))
print("El valor de la primera diferencia finita dividida hacia atrás es:\n", Atras(Ecuacion(X),Ecuacion(X-H)))
print("El valor de la primera diferencia finita dividida centrada es:\n", Centrada(Ecuacion(X+H),Ecuacion(X-H)))
print("El valor verdadero de la segunda derivada son:\n", Ecuacion2(X))
print("El valor de F(X + 2H) es:\n", Ecuacion(X+2*H))
print("El valor de F(X - 2H) es:\n", Ecuacion(X-2*H))
print("El valor de la segunda diferencia finita dividida hacia adelante es:\n", Delante2(Ecuacion(X+2*H),2*Ecuacion(X+H), Ecuacion(X)))
print("El valor de la segunda diferencia finita dividida hacia atrás es:\n",Atras2(Ecuacion(X),2*Ecuacion(X-H),Ecuacion(X-2*H)))
print("El valor de la segunda diferencia finita dividida centrada es:\n", Centrada2(Ecuacion(X+H),2*Ecuacion(X),Ecuacion(X-H)))
print("El valor de la primera diferencia finita dividida centrada con H = 0.05 es:\n", Centrada(Ecuacion(X+0.05),Ecuacion(X-0.05)))
print("El valor de la segunda diferencia finita dividida centrada con H = 0.05 es:\n", Centrada2(Ecuacion(X+0.05),2*Ecuacion(X),Ecuacion(X-0.05)))