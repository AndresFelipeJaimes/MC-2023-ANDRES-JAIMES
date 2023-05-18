import math

def f(x):
    return x**2 - math.exp(-2*x) - 3

def f_prima(x):
    return 2*x + 2*math.exp(-2*x)

def newton_raphson(guess, precision):
    repeticiones= 0
    x = guess
    
    while True:
        repeticiones += 1
        x_next = x - f(x) / f_prima(x)
        
        if abs(x_next - x) < precision:
            break
        
        x = x_next
    
    return round(x, 8), repeticiones

initial_guess = 1.0
precision = 0.5 * 10**-8

raiz, repeticiones = newton_raphson(initial_guess, precision)

print("Raíz estimada:", raiz)
print("Número de iteraciones:", repeticiones)
