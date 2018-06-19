import sys
print(sys.version + "\n")

# 4-10
cars = ['toyota', 'subaru', 'mitsubishi', 'honda', 'jeep', 'ford']
print("The first three items in the list are " + str(cars[:3]))

print("Three items from the middle of the list are " + str(cars[1:4]))

print("The last three items from the list are" + str(cars[-3:]))


# 4-11
my_pizzas = ['pepperoni', 'maragarita', 'sausage', 'cheese', 'spinach']
friend_pizzas = my_pizzas[:]

my_pizzas.append("extra cheese")
friend_pizzas.append("anchovies")

for pizza in my_pizzas:
	print(pizza + " ", end="")
print()

for pizza in friend_pizzas:
	print(pizza + " ", end="")
print()

# 4-12
for pizza in my_pizzas:
	print(pizza)

for pizza in friend_pizzas:
	print(pizza)