# Diccionarios
numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"Nombre": "Carla",
               "Apellido:": "Florida",
               "Altura": 1.60,
               "Edad": 29}
print(information)
del information["Edad"]
print(information)

claves = information.keys()
print(claves)
print(type(claves))
print("\n")

values = information.values()
print(values)
pairs = information.items()
print(pairs)


contacts = {
    "Carla": {
        "Apellido": "Florida",
        "Altura": 1.60,
        "Edad": 29
    },
    "Angel": {
        "Apellido": "Hackerman",
        "Altura": 1.75,
        "Edad": 29
    }
}
print(contacts)
print(contacts['Carla'])
print(contacts['Angel'])