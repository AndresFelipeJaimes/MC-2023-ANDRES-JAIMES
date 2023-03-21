DimensionN = int(input("Ingrese la dimension n de la primera matriz:\n"))
DimensionM = int(input("Ingrese la dimension m de la primera matriz:\n"))
Matriz1 = []
for i in range(DimensionN):
  Fila1 = [0] * DimensionN
  Matriz1.append(Fila1)
print("Ahora, ingrese los valores de la matriz:\n")
for i in range(DimensionN):
  for j in range(DimensionM):
    print("Posicion", i, j)
    M = int(input())
    Matriz1[i][j] = M
DimensionP = int(input("Ingrese la dimension n de la segunda matriz:\n"))
DimensionQ = int(input("Ingrese la dimension m de la segunda matriz:\n"))
Matriz2 = []
for i in range(DimensionP):
  Fila2 = [0] * DimensionP
  Matriz2.append(Fila2)
print("Ahora, ingrese los valores de la matriz:\n")
for i in range(DimensionP):
  for j in range(DimensionQ):
    print("Posicion", i, j)
    M = int(input())
    Matriz2[i][j] = M
print("1. 3 * Matriz1:\n")
for i in range(DimensionN):
  for j in range(DimensionM):
    Matriz1[i][j] = 3 * Matriz1[i][j]
print("El resultado es:\n",  Matriz1)
for i in range(DimensionN):
  for j in range(DimensionM):
    Matriz1[i][j] = Matriz1[i][j] / 3
print("2. 4 * Matriz2:\n")
for i in range(DimensionP):
  for j in range(DimensionQ):
    Matriz2[i][j] = 4 * Matriz2[i][j]
print("El resultado es:\n",  Matriz2)
for i in range(DimensionP):
  for j in range(DimensionQ):
    Matriz2[i][j] = Matriz2[i][j] / 4
print("3. Matriz1 + Matriz2")
if DimensionN == DimensionP and DimensionM == DimensionQ:
  for i in range(DimensionP):
    for j in range(DimensionQ):
      Matriz1[i][j] = Matriz1[i][j] + Matriz2[i][j]
print(Matriz1)
for i in range(DimensionP):
    for j in range(DimensionQ):
      Matriz1[i][j] = Matriz1[i][j] - Matriz2[i][j]
else:
  print("Error, no se pueden sumar porque no tienen el mismo orden")
print("4. Matriz2 * Matriz1:\n")
if DimensionN == DimensionP:
  for i in range(DimensionP):
    for j in range(DimensionQ):
      Matriz1[i][j] = Matriz1[i][j] * Matriz2[i][j]
  print(Matriz1)
else: 
  print("Error, no se pueden multiplicar porque no tienen el orden correcto")
