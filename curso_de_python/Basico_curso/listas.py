
to_do = ["iremos a casa", 
         "hora de comer", 
         "el museo",
         "volver a casa"]
print(to_do)
numbers = [1, 2, 3, 4, "Cinco"]
print(numbers)

del numbers[-1]
print(numbers)

del numbers[:2]
print(numbers)


a = [1, 2, 3, 4, 5]
b = a
print(a)
print(b)
del a[0]
print(id(a))  # imprime el identificador del puntero de esta lista
print(id(b))
print(a)
c = a[:]  # copia los valores del array
print(id(a))
print(id(b))
print(c)
print(id(c))