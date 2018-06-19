# 6-7: People
fr0z3n2 = {
    "first": "logan",
    "last": "stanfield",
    "age": "22",
    "city": "greensboro"
}

TSTER34 = {
    "first": "travis",
    "last": "scarlett",
    "age": "22",
    "location": "hillsborough"
}

garyoak123 = {
    "first": "daniel",
    "last": "titch",
    "age": "22",
    "location": "cary"
}

people = [fr0z3n2, TSTER34, garyoak123]

# Looping through the dictionaries to show the contents.
for person in people:
    for information, details in person.items():
        print(information.title() + ": " + details.title())
    print()

# 6-8: Pets
atticus = {
    "animal": "dog",
    "owner": "nancy"
}

max = {
    "animal": "cat",
    "owner": "ben"
}

oliver = {
    "animal": "cat",
    "owner": "travis"
}

pets = {
    "atticus": atticus,
    "max": max,
    "oliver": oliver
}

for pet_name, pet_details in pets.items():
    print(pet_name.title() + "'s Information:")
    for criteria, detail in pet_details.items():
        print(criteria.title() + ": " + detail.title())
    print()

# 6-9: Favorite Places
favorite_places = {
    "logan": ["japan", "south korea", "california"],
    "daniel": ["japan", "las vegas", "china"],
    # I know Marcus hates virginia, but lel.
    "marcus": ["virginia", "japan", "exon mobile"]
}

for person, their_favorite_places in favorite_places.items():
    print(person.title() + "'s favorite places are ", end="")
    for place in their_favorite_places:
        print(place.title() + " ", end="")
    print()
print()

# 6-10: Favorite Numbers
favorite_numbers = {
	'travis': ['3','6','8','9'],
	'marcus': ['5','1','4','0'],
	'daniel': ['7','5','2','1'],
	'logan': ['8','7','9','2'],
	'will': ['9','5','8','1']
}

for person, favorite_numbers_list in favorite_numbers.items():
    print(person.title() + "'s favorite numbers are ", end = "")
    for favorite_number in favorite_numbers_list:
        print(favorite_number + " ", end = "")
    print()

# 6-11: Cities
cities = {
    "tokyo": {
        "country": "japan",
        "population": "9,000,000",
        "alternate_fact": "tokyo is japan's capital."
    },
    "seoul": {
        "country": "south korea",
        "population": "25,600,000",
        "alternate_fact": "seoul is the capital of south korea"
    },
    "beijing": {
        "country": "china",
        "population": "21,710,000",
        "alternate_fact": "beijing is the capital of china"
    }
}

for city, city_details in cities.items():
    print("Information of " + city.title() + " is below: ")
    for criteria, detail in city_details.items():
        print(criteria.title() + ": " + detail.title())
    print()

# 6-12: Extensions (I skipped this because I get the gist of it.)