# WHY ARE YOU LOOKING AT MY SHIT?

# 6-4 Glossary 2
glossary = {
	'list': "A list is an ordered sequence of items",
	'dictionary': "A dictionary is a data structure in the form of key-value pairs",
	'conditional': "Conditionals are used to evaluate a situation as true or false."
}

for term, definition in glossary.items():
	print(term.title() + ": " + definition)

# 6-5 Rivers
rivers = {
	'yangtze': 'china',
	'nile': 'egypt',
	'niger': 'mali'
}

for river, country in rivers.items():
	print("The " + river.title() + "runs through " + country.title())

for river in rivers:
	print(river.title())

for country in rivers.values():
	print(country.title())

# 6-6 Polling
polled_people = {
	"logan": "swift",
	"john": "python",
	"mike": "java",
	"max": "javascript"
}

people_to_poll = ['logan', 'james', 'harold', 'max', 'carl']

for person in people_to_poll:
	if person not in polled_people:
		print("Please consider taking our survey!")
	else:
		print("Thank you for already participating in our survey!")