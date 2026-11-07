# 2. Imprimir números naturales entre a y d
def imprimir_rango(a, d):
    if a > d:
        return
    else:
        print(a, end=" ")
        imprimir_rango(a + 1, d)

# Prueba
print("Números entre 3 y 8:")
imprimir_rango(3, 8)
print() # Salto de línea