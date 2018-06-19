# 6-1 Person
person = {
	'name': 'travis',
	'last name': 'scarlett',
	'age': 22,
	'city': 'hillsborough'
}

print("This person's information is as follows:\nName: " + 
	person['name'].title() + 
	"\nLast Name: " + person['last name'] +
	"\nAge: " + str(person['age']) +
	"\nCity: " + person['city'].title())

# 6-2 Favorite Numbers
favorite_numbers = {
	'travis': 3,
	'marcus': 5,
	'daniel': 7,
	'logan': 8,
	'will': 9
}

print("My friend's favorite numbers are:")
print("Will: " + str(favorite_numbers['travis']) +
	  "\nMarcus: " + str(favorite_numbers['marcus']) +
	  "\nDaniel: " + str(favorite_numbers['daniel']) +
	  "\nLogan: " + str(favorite_numbers['logan']) + 
	  "\nTravis: " + str(favorite_numbers['travis']))

# 6-3 Glossary
glossary = {
	'lists': "Lists contain a list of similar objects.",
	'dictionaries': "A structure for key-value pairs"
}

print(glossary['lists'])
print(glossary['dictionaries'])