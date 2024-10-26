# Ejemplo de iterador

# Crear una lista
my_list = [1, 2, 3, 4]

# Obtener el iterador
my_iter = iter(my_list)

# Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# Iteradores de Texto
text = "Hola Mundo"
iter_text = iter(text)

# iterar la cadena
for char in iter_text:
  print(char)

# Iterador de numeros impares
# Limite
limit = 10

# Crear iterador de numeros impares
odd_iter = iter(range(1, limit+1, 2))

# Usar el iterador 
for num in odd_iter:
  print(num)