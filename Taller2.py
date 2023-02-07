A = {6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
B = {2,4,6,8,10,12,14,16,18,20,22,24}
C = {1,4,8,10,12,15,18,20}
D = {2,3,5,7,11,13,17,19,23,29,31,37,41,43}
print("Conjunto A.\n", A)
print("Conjunto B.\n", B)
print("Conjunto C.\n", C)
print("Conjunto D.\n", D)

def Union(Conj1, Conj2):
  Conj3 = Conj1|Conj2
  return Conj3
def Interseccion(Conj1, Conj2):
  Conj3 = Conj1&Conj2
  return Conj3
def Diferencia(Conj1, Conj2):
  Conj3 = Conj1-Conj2
  return Conj3
def DiferenciaSimetrica(Conj1, Conj2):
  Conj3 = Conj1^Conj2
  return Conj3
#Operacion1
Operacion1 = Interseccion(B, DiferenciaSimetrica(C,D))
print("Operacion 1.\n", Operacion1)
#Operacion2
Operacion2 = Union(Interseccion(A,C), B)
print("Operacion 2.\n", Operacion2)
#Operacion3
Operacion3 = Diferencia(Union(B,D), C)
print("Operacion 3.\n", Operacion3)
#Operacion4
Operacion4 = DiferenciaSimetrica(Diferencia(A,B), Interseccion(A,D))
print("Operacion 4.\n", Operacion4)