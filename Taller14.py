import copy
from itertools import count
from re import A

def matrix_format(matriz, formato):
    n_rows = len(matriz)
    n_cols = len(matriz[0])


    col_max_width = []
    for col in range(n_cols):
        max_width = 0
        for row in range(n_rows):
           
            edit_value = formato % matriz[row][col]
            max_width = max(max_width, len(edit_value))
        col_max_width.append(max_width)

    salida = []
    for row in range(n_rows):
        edit_row = []
        for col in range(n_cols):
           
            edit_value = formato % matriz[row][col]
           
            edit_space = " "*(col_max_width[col] - len(edit_value))
            edit_row.append("%s%s" % (edit_space, edit_value))
        salida.append(edit_row)
   
    return salida

def imprimirEcuaciones(a, b):
    salida = matrix_format(a, " %.1f")
    i = 0
    for row in salida:
        for col in row:
            print(col, end="  ")
        print("| " + str(b[i]))
        i += 1


def gaussJordan(a, b):
    aAux = copy.deepcopy(a)
    bAux = copy.deepcopy(b)

    n = len(bAux)

    print("Ecuaciones")
    imprimirEcuaciones(aAux, bAux)
    print()

   
    count = 1
    count2 = 1
    for i in range(n):
        if aAux[i][i] == 0:
            for c in range(n):
                if aAux[c][i] != 0:
                    tempA = aAux[i]
                    tempB = bAux[i]
                    aAux[i] = aAux[c]
                    aAux[c] = tempA
                    bAux[i] = bAux[c]
                    bAux[c] = tempB
                    print("Normalizacion " + str(count))
                    imprimirEcuaciones(aAux, bAux)
                    print()
                    count += 1
        div = aAux[i][i]
        for e in range(n):
            aAux[i][e] /= div
        bAux[i] /= div
        for j in range(n):
            if i != j:
                fact = -aAux[j][i] / aAux[i][i]
                for k in range(n):
                    aAux[j][k] += (aAux[i][k] * fact)

                bAux[j] += (bAux[i] * fact)

                print("Reducción " + str(count2))
                imprimirEcuaciones(aAux, bAux)
                print()
                count2 += 1

    return bAux


a = []
b = []

print("Solucion de ecuaciones por Gauss Jordan")
dim = int(input("Ingrese el numero de incognitas y ecuaciones: "))
for i in range(dim):
    newFila = []
    print("\nCoeficientes de la ecuacion "+str(i+1))
    for j in range(dim):
        newFila.append(float(input("X"+str(j+1)+": ")))
    a.append(newFila)
    newA = a

for j in range(dim):
    print("\nIgualdad de la ecuacion "+str(j+1))
    b.append(float(input("Igualdad: ")))

print("\n")
x = gaussJordan(a, b)

#Se imprimen los resultados
for i in range(len(x)):
    print("x" + str(i + 1) + " = " + str(x[i]))

print()