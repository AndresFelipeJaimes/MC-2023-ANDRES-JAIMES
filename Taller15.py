DimensionN = int(input("Ingrese la dimension n de la primera matriz:\n"))
Matriz1 = []
for i in range(DimensionN):
  Fila1 = [0] * DimensionN
  Matriz1.append(Fila1)
print("Ahora, ingrese los valores de la matriz:\n")
for i in range(DimensionN):
  for j in range(DimensionN):
    print("Posicion", i, j)
    M = int(input())
    Matriz1[i][j] = M
Matriz2 = [[0 for x in range(DimensionN)] for y in range(DimensionN)]
for i in range(DimensionN):
    Matriz2[i][i] = 1
Matriz3 = [fila_A + fila_B for fila_A, fila_B in zip(Matriz1, Matriz2)]
def GaussJordan(Matriz3):
    Matriz3 = [[float(j) for j in i] for i in Matriz3]
    for fila in range(DimensionN):
        if Matriz3[fila][fila] == 0:
            for fila2 in range(fila + 1, DimensionN):
                if Matriz3[fila2][fila] != 0:
                    Matriz3[fila], Matriz3[fila2] = Matriz3[fila2], Matriz3[fila]
                    break
        divisor = Matriz3[fila][fila]
        Matriz3[fila] = [elem / divisor for elem in Matriz3[fila]]
        for fila2 in range(DimensionN):
            if fila2 != fila:
                factor = Matriz3[fila2][fila]
                Matriz3[fila2] = [elem1 - factor * elem2 for elem1, elem2 in zip(Matriz3[fila2], Matriz3[fila])]
    return Matriz3
GaussJordan(Matriz3)