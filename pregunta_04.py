# 4. Calcular x^y mediante multiplicaciones sucesivas
def potencia(x, y):
    if y == 0:
        return 1
    else:
        return x * potencia(x, y - 1)

# Prueba
print("2 elevado a la 4:", potencia(2, 4))