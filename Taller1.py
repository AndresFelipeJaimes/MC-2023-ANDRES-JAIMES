print("Hola usuario. Por favor, ingrese la extension de los conjuntos")
Conjunto1 = set()
Conjunto2 = set()
ExtensionConjunto1= int(input("Ingrese la extension del primer conjunto: \n"))
print("Ahora ingrese los elementos del primer conjunto.")
i = 0
while (i < ExtensionConjunto1):
  ValorConjunto1= float(input("Ingrese el valor: \n"))
  Conjunto1.add(ValorConjunto1)
  i= i+1
print("El conjunto 1 es igual a : \n", Conjunto1)
ExtensionConjunto2= int(input("Ingrese la extension del segundo conjunto: \n"))
print("Ahora ingrese los elementos del primer conjunto.")
j = 0
while (j < ExtensionConjunto2):
  ValorConjunto2= float(input("Ingrese el valor: \n"))
  Conjunto2.add(ValorConjunto2)
  j= j+1
print("El conjunto 2 es igual a : \n", Conjunto2)
OpcionMenu = int(input("Ahora, seleccione la operacion que desea realizar.\n 1. Union.\n 2. Interseccion.\n 3. Diferencia.\n 4. Diferencia simetrica.\n 5. Salir\n"))
if OpcionMenu == 1: #Union
  Conjunto3 = Conjunto1|Conjunto2
  print("El resultado de la union de ambos conjuntos es: ", Conjunto3, "\nLa longitud del conjunto resultante es: ", len(Conjunto3))
elif OpcionMenu == 2: #Interseccion
  Conjunto3 = Conjunto1&Conjunto2
  print("El resultado de la interseccion de ambos conjuntos es: ", Conjunto3, "\nLa longitud del conjunto resultante es: ", len(Conjunto3))
elif OpcionMenu == 3: #Diferencia
  Conjunto3 = Conjunto1-Conjunto2
  print("El resultado de la diferencia de ambos conjuntos es: ", Conjunto3, "\nLa longitud del conjunto resultante es: ", len(Conjunto3))
elif OpcionMenu == 4: #Diferencia simetrica
  Conjunto3 = Conjunto1^Conjunto2
  print("El resultado de la diferencia simetrica de ambos conjuntos es: ", Conjunto3, "\nLa longitud del conjunto resultante es: ", len(Conjunto3))
elif OpcionMenu == 5:
  print("Hasta luego")
else:
  print("Opcion Incorrecta")