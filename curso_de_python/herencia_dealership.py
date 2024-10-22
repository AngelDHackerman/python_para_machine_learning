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