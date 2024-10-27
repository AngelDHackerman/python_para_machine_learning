def check_access(func):
  def wrapper(employee):
    # comprobar si el empleado tiene role 'admin'
    if employee.get('role') == 'admin':
      return func(employee)
    else:
      print('ACCESSO DENEGADO. Solo los administradores pueden acceder.')
  return wrapper


@check_access
def delete_employee(employee):
  print(f"Empleado {employee['name']} ha sido eliminado")
  
admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'usr'}

delete_employee(admin)
# delete_employee(employee)