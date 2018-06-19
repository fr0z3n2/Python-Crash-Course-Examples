import sys
print (sys.version)

# 4-1
pizzas = ['pepperoni', 'maragarita', 'sausage', 'cheese', 'spinach']

for pizza in pizzas:
    print('I like ' + pizza + ' pizza!')

print("I like " + pizzas[0])
print("I like " + pizzas[3])
print("I like " + pizzas[4])
print('Boy, I sure do like pizza')

# 4-2
animals = ['cat', 'dog', 'lizard', 'sponge']
for animal in animals:
    print('A ' + animal + ' would make a great pet')

print('Any of these animals would make a great pet!')

# Me messing around with the range() function
numbers = list(range(1,6))
print(numbers)
