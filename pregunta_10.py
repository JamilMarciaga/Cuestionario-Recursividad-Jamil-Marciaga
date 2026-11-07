# 10. Calcular C(n,k)
def combinaciones(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combinaciones(n - 1, k - 1) + combinaciones(n - 1, k)

# Prueba
print("Combinaciones C(5, 2):", combinaciones(5, 2))