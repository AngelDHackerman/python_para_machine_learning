import json 

# Lectura del json 
with open('./productos.json', mode='r') as file:
  products = json.load(file)
  
# Mostrar el contenido
for product in products:
  print(f"Product: {product['name']}, Price: {product['price']}")