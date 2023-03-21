Vector1 = []
Vector2 = []
Acumulador = 0
Dimension = int(input("Hola usuario. Por favor, ingrese la longitud del vector que quiere calcular:\n"))
print ("Vector 1.")
for i in range(Dimension):
  print("Posicion", i)
  Valor1 = int(input())
  Vector1.append(Valor1)
print("Vector 2.")
for j in range(Dimension):
  print("Posicion", j)
  Valor2 = int(input())
  Vector2.append(Valor2)
for k in range(Dimension):
    Resultado = Vector1[k] * Vector2[k]
    Acumulador = Resultado + Acumulador
print("El resultado del producto escalar es:\n", Acumulador)