numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))

# Multiples iterables: 
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))