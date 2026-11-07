# 3. Cantidad de dígitos de un número entero
def contar_digitos(n):
    n = abs(n) 
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

# Prueba
print("Dígitos de 2024:", contar_digitos(2024))