set_countries = {'Col', 'Mex', 'Bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 3, 4, 4, 5, 829}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hoola')  # {'h', 'o', 'l', 'a'}
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers = [1, 2, 3, 4, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)