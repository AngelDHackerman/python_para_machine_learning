class Person: 
  # Este es el constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def great(self):
    print(f"Hola, mi nombre es {self.name} y tengo {self.age} años de edad.")
    
person1 = Person("Ana", 30)
person2 = Person("Luis", 25)

person1.great()
person2.great() 