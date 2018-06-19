# 5-8
active_users = ["admin", "speeddemon64", "fr0z3n2", "TSTER34", "garyoak123"]
# Comment out the line below to loop through the list of users.
active_users = []

if active_users:
	for user in active_users:
		if user == "admin":
			print("Welcome Administrator! Would you like a status report?")
		else:
			print("Welcome " + user + "!")
else:
	print("There are currently no active users.")
# 5-9 Adds the initial if statement.

# 5-10: Checking usernames

current_users = ["fr0z3n2", "TSTER34", "SPEEDDEMON64", "garyoak123", "Waldo57"]
new_users = ["lgstanfi", "pika_pan22", "fr0z3n2", "scrooge567", 
	"Xx BigButts 420 xX", "BLAZEitPRAISEIT", "fr0z3n5", "speeddemon64"]

current_users_lower = [curr_user.lower() for curr_user in current_users]

for user in new_users:
	if user.lower() in current_users_lower:
		print("Username taken! Please enter a new name. (Case insensitive")
	else:
		print("New user added!")

# 5-11 (Ordinal numbers)
numbers = [number for number in range(1,10)]

for number in numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print(str(number) + "nd")
	elif number == 3:
		print(str(number) + "rd")
	else:
		print(str(number) + "th")
