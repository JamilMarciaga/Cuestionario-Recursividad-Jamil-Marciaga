# 7. Contar secuencias de dos 1 seguidos en un binario
def contar_unos_seguidos(binario, indice=0):
    if indice >= len(binario) - 1:
        return 0
    
    if binario[indice] == '1' and binario[indice+1] == '1':
        return 1 + contar_unos_seguidos(binario, indice + 1)
    else:
        return contar_unos_seguidos(binario, indice + 1)

# Prueba
cadena_binaria = "110111011"
print(f"Secuencias de '11' en {cadena_binaria}:", contar_unos_seguidos(cadena_binaria))