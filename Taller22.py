import numpy as np

# Función de interpolación de Lagrange
def lagrange_interpolation(x, y, x_ingresado, grado):
    y_estimacion = 0
    
    for i in range(grado+1):
        valor_y = y[i]
        for j in range(grado+1):
            if j != i:
                valor_y *= (x_ingresado - x[j]) / (x[i] - x[j])
        y_estimacion += valor_y
    
    return y_estimacion

# Inicio del programa
if __name__ == "__main__":
    # Ingresar puntos
    n = int(input("Ingrese el numero de puntos: "))
    x = np.zeros(n)
    y = np.zeros(n)
    
    for i in range(n):
        x[i] = float(input(f"Ingrese el valor de x{i+1}: "))
        y[i] = float(input(f"Ingrese el valor de y{i+1}: "))
    
    # Ingresar el valor de x a estimar
    x_ingresado = float(input("Ingrese el valor de x a estimar: "))
    
    # Estimaciones de interpolación de Lagrange para diferentes grados
    y_est1 = lagrange_interpolation(x, y, x_ingresado, 1)
    print(f"La estimación para el grado 1 es: {y_est3}")
    
    y_est2 = lagrange_interpolation(x, y, x_ingresado, 2)
    print(f"La estimación para el grado 2 es: {y_est2}")
    
    y_est3 = lagrange_interpolation(x, y, x_ingresado, 3)
    print(f"La estimación para el grado 3 es: {y_est1}")