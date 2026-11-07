# 6. Valor máximo de un vector de componentes numéricas
def maximo_vector(vector, indice=0):
    if indice == len(vector) - 1:
        return vector[indice]
    
    max_resto = maximo_vector(vector, indice + 1)
    
    if vector[indice] > max_resto:
        return vector[indice]
    else:
        return max_resto

# Prueba
mi_vector = [3, 8, 15, 2]
print("El máximo del vector [3, 8, 15, 2] es:", maximo_vector(mi_vector))