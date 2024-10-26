while True:
  try:
    divisor = int(input("ingresa un numero divisor: "))
    result = 100 / divisor
    print(result)
    break
  except ZeroDivisionError as e:
    print("Error: el divisor no puede ser cero")
    print("Ha occurido un error: ", e)
  except ValueError as e:
    print("Error: Debes introducir un numero valido")
    print("Ha occurido un error: ", e)
  