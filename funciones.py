def es_primo(n):
    """Retorna True si n es un número primo, de lo contrario retorna False."""
    if n < 2:
        return False
    # Solo necesitamos comprobar divisores hasta la raíz cuadrada de n.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ejemplo de uso:
numero = 17
if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")
