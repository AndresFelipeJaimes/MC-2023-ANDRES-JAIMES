import numpy as np
# Variables de trabajo
St = 0
Sr = 0
SumaX12 = 0
SumaX22 = 0
SumaX1X2 = 0
SumaX1Y = 0
SumaX2Y = 0
# Datos de la tabla
X1 = [1, 1, 2, 3, 1, 2, 3, 3]
X2 = [0, 1, 1, 2, 2, 3, 3, 1]
Y = [3.2, 6, 2.2, 2.5, 6.5, 6.6, 3.5, 0.2]
# Coeficientes sistema de ecuaciones
n = len(Y)
SumaY = np.sum(Y)
PromedioY = np.mean(Y)
SumaX1 = np.sum(X1)
SumaX2 = np.sum(X2)
for i in range(n):
  Ciclo= X1[i]**2
  SumaX12 = Ciclo + SumaX12
for i in range(n):
  Ciclo= X2[i]**2
  SumaX22 = Ciclo + SumaX22
for i in range(n):
  Ciclo= X1[i]*X2[i]
  SumaX1X2 = Ciclo + SumaX1X2 
for i in range(n):
  Ciclo= X1[i]*Y[i]
  SumaX1Y = Ciclo + SumaX1Y
for i in range(n):
  Ciclo= X2[i]*Y[i]
  SumaX2Y = Ciclo + SumaX2Y 
# Hallar St
for i in range(n):
  Ciclo= (Y[i] - PromedioY)**2
  St = Ciclo + St
# Gauss-Jordan
A = np.array([[n, SumaX1, SumaX2], [SumaX1, SumaX12, SumaX1X2], [SumaX2, SumaX1X2, SumaX22]])
B = np.array([SumaY, SumaX1Y, SumaX2Y])
X = np.linalg.solve(A, B)
# Hallar Sr
for i in range(n):
  Ciclo= (Y[i] - X[0] - (X[1]*X1[i]) -(X[2]*X2[i]))**2
  Sr = Ciclo + Sr
print(" El resultado de a0 es:", X[0])
print(" El resultado de a1 es:", X[1])
print(" El resultado de a2 es:", X[2])
print(" El resultado de la ecuacion es: y=", X[0], "+" , X[1], "X1-", X[2], "X2"  )
print(" El resultado de St es:", St)
print(" El resultado de Sr es:", Sr)