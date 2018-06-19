# 4-3
values = [value for value in range(1,21)]
print(values)

# 4-4
million = [value for value in range(1,1000001)]
print(max(million))
print(min(million))

# 4-5
print(sum(million))

# 4-6
# This is one way of obtaining all of the odd numbers
odd_numbers = [2 * value + 1 for value in range(0, 10)]
print(odd_numbers)

# This is the better way of getting all of the odd numbers
odd_numbers = [value for value in range(1, 21, 2)]
print(odd_numbers)

# 4-7
multiples_of_three = [value * 3 for value in range(3, 31)]
for multiple in multiples_of_three:
	print(multiple)


# 4-8
print("4-8")
cubes = []
for value in range(1,11):
	cubes.append(value ** 3)
print(cubes)

# 4-9
print("4-9")
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)