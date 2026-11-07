# 1. Suma de los n primeros números naturales
def suma_naturales(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + suma_naturales(n - 1)

# Prueba
print("Suma de los primeros 5 naturales:", suma_naturales(5))