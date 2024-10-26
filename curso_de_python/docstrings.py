def dividir(a, b):
    """
    Devuelve el cociente de dos números.
    
    Parámetros:
    a (int o float): El numerador.
    b (int o float): El denominador. No debe ser cero.
    
    Retorna:
    float: El resultado de la división.
    
    Excepciones:
    ZeroDivisionError: Si b es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


print(dividir(10, 2))