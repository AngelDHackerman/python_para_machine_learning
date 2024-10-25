# Diccionario de ejemplo
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Aplicar map() a las claves del diccionario
new_keys = map(str.upper, my_dict.keys())
# print(list(new_keys))

# Crear un nuevo diccionario con las claves transformadas
new_dict = dict(zip(new_keys, my_dict.values()))

print(new_dict)