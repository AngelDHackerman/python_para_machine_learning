def check_access(required_role):
    # Esta función recibe el parámetro 'required_role' cuando se define el decorador
    def decorator(func):
        # Esta función es la que recibe la función que se va a decorar (como delete_employee)
        def wrapper(employee):
            # Esta es la función que añade la lógica (verificar el rol del empleado)
            if employee.get('role') == required_role:
                return func(employee)  # Si pasa la condición, llama a la función original
            else:
                print(f'ACCESSO DENEGADO. Solo {required_role} pueden realizar esta acción.')
        return wrapper  # Devuelve la función wrapper, que sustituye a la original
    return decorator  # Devuelve el decorador que realmente decora la función

def log_action(func):
  def wrapper(employee):
    print(f"Registrando accion para el empleado {employee['name']}")
    return func(employee)
  return wrapper

@check_access('admin')
@log_action
def delete_employee(employee):
  print(f'El empleado {employee['name']},ha sido eliminado')
  
admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'usr'}

delete_employee(admin)
# delete_employee(employee)
