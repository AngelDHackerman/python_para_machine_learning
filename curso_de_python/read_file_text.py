# Leer un archivo linea por linea

# with open('./caperucita.txt', 'r') as file:
#   for lineas in file:
#     print(lineas.strip())

# Leer todas las lineas en una lista
# with open('caperucita.txt', 'r') as file:
#   lines = file.readlines()
#   print(lines)

# Agregar texto, con 'w' se sobreescribe
with open('caperucita.txt', 'a') as file:
  file.write("\n\nBy:Angel Hackerman")