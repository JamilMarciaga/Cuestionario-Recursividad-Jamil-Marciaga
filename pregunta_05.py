# 5. Calcular x*y mediante sumas sucesivas
def multiplicacion_sumas(x, y):
    if y == 0:
        return 0
    elif y < 0:
        return -x + multiplicacion_sumas(x, y + 1)
    else:
        return x + multiplicacion_sumas(x, y - 1)

# Prueba
print("4 multiplicado por 3:", multiplicacion_sumas(4, 3))