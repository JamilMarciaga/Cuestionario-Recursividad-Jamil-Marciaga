# 8. Hexadecimal a Decimal
def hex_a_decimal(cadena, longitud):
    if longitud == 0:
        return 0
    
    caracter = cadena[0].lower()
    if '0' <= caracter <= '9':
        valor = int(caracter)
    elif 'a' <= caracter <= 'f':
        valor = ord(caracter) - ord('a') + 10
        
    return valor * (16 ** (longitud - 1)) + hex_a_decimal(cadena[1:], longitud - 1)

# Prueba
hex_str = "1A3"
print(f"El hexadecimal {hex_str} en decimal es:", hex_a_decimal(hex_str, len(hex_str)))