def metodo_biseccion(a, b, epsilon):
    max_iteraciones = 1000
    iteracion = 1
    c = 0

    while iteracion <= max_iteraciones:
        c = (a + b) / 2

        if abs(f(c)) < epsilon:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iteracion += 1

    return c, iteracion

def f(x):
    # Función: 1.5x^3 - 3.5x^2 - 2x + 2
    return 1.5 * x**3 - 3.5 * x**2 - 2 * x + 2

# Parámetros iniciales
a = 0.5  # Límite inferior del intervalo
b = 1  # Límite superior del intervalo
epsilon = 0.0001  # Tolerancia de error

# Aplicar el método de la bisección
resultado, num_iteraciones = metodo_biseccion(a, b, epsilon)

# Imprimir resultados
print("La raíz aproximada es:", resultado)
print("Error aproximado:", f(resultado))
print("Número de iteraciones:", num_iteraciones)