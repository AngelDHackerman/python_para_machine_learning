# Los closures son las funciones que "recuerdan"

# Ejemplo con strings
def exterior(mensaje):
  """funcion externa que crea un closure"""
  def interior():
    """Funcion anidad que usa la variable de la funcion externa"""
    print(mensaje)
  return interior

mi_funcion = exterior("Hola, mundo!")
mi_funcion()

# Ejemplo con matematicas
def suma_constante(n):
  """Devuelve una funcion que suma un valor constante a otro numero"""
  def suma(valor):
    return valor + n
  return suma

sumar_5 = suma_constante(5)
sumar_10 = suma_constante(10)

print(sumar_5(2)) # 7
print(sumar_10(4)) # 14