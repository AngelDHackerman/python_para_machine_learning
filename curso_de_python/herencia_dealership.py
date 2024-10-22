class Vehicle:
  def __init__(self, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price
    self.is_available = True
    
  def sell (self):
    if self.is_available:
      self.is_available = False
      print(f"El vehiculo {self.brand}. Ha sido vendido")
    else:
      print(f"El vehiculo {self.brand}. No esta disponible")
      
  def check_available(self):
    return self.is_available
  
  def get_price(self):
    return self.price
  
  def start_engine(self):
    raise NotImplementedError("Este medoto debe ser impelmentado por la subclase")
  
  def stop_engine(self):
    raise NotImplementedError("Este medoto debe ser impelmentado por la subclase")
  
# Sub-clases

class Car(Vehicle):
  def start_engine(self):
    if not self.is_available:
      return f"El motor del coche {self.brand} esta en marcha"
    else:
      return f"El coche {self.brand} no esta disponible"
    
  def stop_engine(self):
    if not self.is_available:
      return f"El motor del coche {self.brand} se ha detenido"
    else:
      return f"El coche {self.brand} no esta disponible."
    
class Bike(Vehicle):
  def start_engine(self):
    if not self.is_available:
      return f"La bicicleta {self.brand} esta en marcha"
    else:
      return f"El bicicleta {self.brand} no esta disponible"
    
  def stop_engine(self):
    if not self.is_available:
      return f"La bicicleta {self.brand} se ha detenido"
    else:
      return f"La bicicleta {self.brand} No esta diponible"
    
class Truck(Vehicle):
  def start_engine(self):
    if not self.is_available:
      return f"El motor del camion {self.brand} esta en marcha"
    else:
      return f"El camion {self.brand} no esta disponible"
  
  def stop_engine(self):
    if not self.is_available:
      return f"El motor del camion {self.brand} se ha detenido"
    else:
      return f"El camion {self.brand} no esta disponible."
    
class Customer:
  def __init__(self, name):
    self.name = name
    self.purchased_vehicle = []
    
  def buy_vehicle(self, vehicle: Vehicle):
    if vehicle.check_available():
      vehicle.sell()
      self.purchased_vehicle.append(vehicle)
    else:
      print(f"Lo siento, {vehicle.brand} no esta disponible")
    
  def inquire_vehicle(self, vehicle: Vehicle):
    if vehicle.check_available():
      availability = "Disponible"
    else:
      availability = "No disponible"
    print(f"El {vehicle.brand} esta {availability} y cuesta {vehicle.get_price()}")
    
class Dealership:
  def __init__(self):
    self.inventory = []
    self.customers = []
    
  def add_vehicle(self, vehicle: Vehicle):
    self.inventory.append(vehicle)
    print(f"El {vehicle.brand} ha sido añadido al inventario")
    
  def register_customer(self, customer: Customer):
    self.customers.append(customer)
    print(f"El cliente {customer.name} ha sido añadido")
    
  def show_available_vehicles(self):
    print("Vehiculos disponibles en la tienda")
    for vehicle in self.inventory:
      if vehicle.check_available():
        print(f"- {vehicle.brand} - {vehicle.model} por {vehicle.get_price()}")