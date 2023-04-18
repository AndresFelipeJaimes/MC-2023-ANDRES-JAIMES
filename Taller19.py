from math import sqrt
X = [1,2,3,4,5,6,7]
Y = [0.2, 0.5, 1.8, 3.4, 5.7, 9.0, 13.8]
Multiplicacion = 0
SumaX = 0
SumaY = 0
SumaX2 = 0
SumaX3 = 0
St = 0
Sr = 0
n = len(X)
for i in range(n):
  Multiplicacion = X[i]*Y[i] + Multiplicacion
  SumaX = X[i] + SumaX
  SumaY = Y[i] + SumaY
  SumaX2 = (X[i] ** 2) + SumaX2
Resultado = (n * Multiplicacion - SumaY*SumaX)/ (n*SumaX2 - (SumaX**2))
Resultado2 = (SumaY/n) - Resultado*(SumaX/n)
PromedioY = SumaY / 7
for i in range(n):
  Ciclo= (Y[i] - PromedioY)**2
  St = Ciclo + St
for i in range(n):
  Ciclo = (Y[i]-Resultado2-(Resultado*X[i]))**2
  Sr = Ciclo + Sr
Sy = sqrt(St/(n-1))
Syx = sqrt(Sr/(n-2))
r = sqrt((St-Sr)/St) * 100
print("El resultado de a1 es: ", Resultado)
print("El resultado de a0 es: ", Resultado2)
print("El resultado del promedio de Y es: ", PromedioY)
print("El resultado de St es: ", St)
print("El resultado de Sy es: ", Sy)
print("El resultado de Sr es: ", Sr)
print("El resultado de Sy/x es: ", Syx)
print("El resultado de r es: ", r, "%")