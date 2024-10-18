squares = [x**2 for x in range(1, 11)]
print("Cuadrados:", squares)

# Conversor temperatura
celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = [(9/5 * c) + 32 for c in celsius]
print("Conversion Fahrenheit:", fahrenheit)

# Numeros pares
evens = [x for x in range(1, 21) if x%2 == 0]
print(f"Numeros pares: {evens}")

matrix = [[1, 2, 3],
          [4, 5, 6,],
          [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)