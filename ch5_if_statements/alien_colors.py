# 5-3 Aliens
alien_color = 'red'

if alien_color == 'green':
	print("You just got +5 points")

# 5-4
if alien_color == 'green':
	print("You just got +5 points.")
else:
	print("You just got +10 points!")

# 5-5
if alien_color == 'green':
	print("You just got +5 points.")
elif alien_color == 'yellow':
	print("You just got +10 points!")
elif alien_color == 'red':
	print("You just got +15 points!!")
else:
	print("No points added.")

# 5-6
age = 19

# Checking to see what stage of life the person is in.
if age < 2:
	print("You are a baby")
elif age < 4:
	print("You are a toddler")
elif age < 13:
	print("Sorry kiddo!")
elif age < 20:
	print("You are a teenager")
elif age < 65:
	print("You are an adult. Time to pay bills ;)")
else:
	print("You are so old! :)")

# 5-7
favorite_fruits = ["peach", "strawberry", "lemon", "grape"]

if "peach" in favorite_fruits:
	print("You really like peaches!")
if "strawberry" in favorite_fruits:
	print("You really like strawberry!")
if "watermelon" in favorite_fruits:
	print("You really like watermelon!")
if "grape" in favorite_fruits:
	print("You really like grapes!")
if "blueberry" in favorite_fruits:
	print("You really like blueberry!")