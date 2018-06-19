# Author: Logan Stanfield
# Date: 05/16/18
# Description: This is me fumbling with lists in Python 3. These exercises come
#   from the book.

# 3-1
my_friends = ["Mike", "Nez", "Jess", 'Brandon H.']
print(my_friends[1])

# 3-2
print("Greetings " + my_friends[0] + "! How are you?")
print("Greetings " + my_friends[1] + "! How are you?")
print("Greetings " + my_friends[2] + "! How are you?")
print("Greetings " + my_friends[3] + "! How are you?")

# 3-3
vehicles = ["car", "truck", "bicycle", "boat"]
print("I would love to own a " + vehicles[-1] + "!")
print("I would love to ride a " + vehicles[-2] + "!")

# 3-4
people_to_invite = ['Nancy', 'Manfred', 'Ben', 'Travis', 'Daniel', 'Marcus', 'Will', 'Dylan', 'Harry']
print("Hey " + people_to_invite[0] + "! You're invited to dinner!")
print("Hey " + people_to_invite[1] + "! You're invited to dinner!")
print("Hey " + people_to_invite[2] + "! You're invited to dinner!")
print("Hey " + people_to_invite[3] + "! You're invited to dinner!")
print("Hey " + people_to_invite[4] + "! You're invited to dinner!")
print("Hey " + people_to_invite[5] + "! You're invited to dinner!")
print("Hey " + people_to_invite[6] + "! You're invited to dinner!")
print("Hey " + people_to_invite[7] + "! You're invited to dinner!")
print("Hey " + people_to_invite[8] + "! You're invited to dinner!")

# 3-5
print(people_to_invite)
print(people_to_invite.pop(3) + " can't make it")
people_to_invite.insert(3, "Mike")
print(people_to_invite)

print("Hey " + people_to_invite[0] + "! You're invited to dinner!")
print("Hey " + people_to_invite[1] + "! You're invited to dinner!")
print("Hey " + people_to_invite[2] + "! You're invited to dinner!")
print("Hey " + people_to_invite[3] + "! You're invited to dinner!")
print("Hey " + people_to_invite[4] + "! You're invited to dinner!")
print("Hey " + people_to_invite[5] + "! You're invited to dinner!")
print("Hey " + people_to_invite[6] + "! You're invited to dinner!")
print("Hey " + people_to_invite[7] + "! You're invited to dinner!")
print("Hey " + people_to_invite[8] + "! You're invited to dinner!")

# 3-6
print("Hey guys! Check out this bigger table!! :O")
print(len(people_to_invite))
people_to_invite.insert(0, "Even")
print(people_to_invite)
people_to_invite.insert(len(people_to_invite) // 2, "Guy McMiddle")
print(people_to_invite)
people_to_invite.append('Jimmy Endman')
print(people_to_invite)

print("Hey " + people_to_invite[0] + "! You're invited to dinner!")
print("Hey " + people_to_invite[1] + "! You're invited to dinner!")
print("Hey " + people_to_invite[2] + "! You're invited to dinner!")
print("Hey " + people_to_invite[3] + "! You're invited to dinner!")
print("Hey " + people_to_invite[4] + "! You're invited to dinner!")
print("Hey " + people_to_invite[5] + "! You're invited to dinner!")
print("Hey " + people_to_invite[6] + "! You're invited to dinner!")
print("Hey " + people_to_invite[7] + "! You're invited to dinner!")
print("Hey " + people_to_invite[8] + "! You're invited to dinner!")
print("Hey " + people_to_invite[6] + "! You're invited to dinner!")
print("Hey " + people_to_invite[7] + "! You're invited to dinner!")
print("Hey " + people_to_invite[8] + "! You're invited to dinner!")
print("Hey " + people_to_invite[9] + "! You're invited to dinner!")
print("Hey " + people_to_invite[10] + "! You're invited to dinner!")
print("Hey " + people_to_invite[11] + "! You're invited to dinner!")

# 3-7
print("Sorry guys! I can only invite two people tp dinner :(")
print("Sorry, you can't make it to dinner " + people_to_invite.pop())
print("Sorry, you can't make it to dinner " + people_to_invite.pop())
print("Sorry, you can't make it to dinner " + people_to_invite.pop())
print("Sorry, you can't make it to dinner " + people_to_invite.pop())
print("Sorry, you can't make it to dinner " + people_to_invite.pop())
print("Sorry, you can't make it to dinner " + people_to_invite.pop())
print("Sorry, you can't make it to dinner " + people_to_invite.pop())
print("Sorry, you can't make it to dinner " + people_to_invite.pop())
print("Sorry, you can't make it to dinner " + people_to_invite.pop())
print("Sorry, you can't make it to dinner " + people_to_invite.pop())
print(people_to_invite)

print(people_to_invite[0].title() + ", you're still invited")
print(people_to_invite[1].title() + ", you're still invited")

del people_to_invite[0]
del people_to_invite[0]

print(people_to_invite)

# Testing random stuff
cars = ['bmw', 'toyota', 'subaru', 'audi']
# cars.sort is not stored to cars_sorted.
cars_sorted = cars.sort()
print(cars)
print(cars_sorted)

# Testing out more sorting stuff
cars = ['bmw', 'toyota', 'subaru', 'audi']
cars_sorted = sorted(cars)
print("The sorted cars are" + str(cars_sorted))
print(cars)

# 3-8
places_to_visit = ["Tokyo", "Seoul", "Hong Kong", "Los Angeles", "New York City"]
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print(sorted(places_to_visit, reverse = True))
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse = True)
print(places_to_visit)

people_to_invite = ["Travis", "Daniel", "Marcus", "Will", "Dylan"]
print(len(people_to_invite))

video_game_list = ["Mother 2", "Final Fantasy XIII", "Halo 2", "Garry's Mod", "Persona 5"]
video_game_list.append("Grand Theft Auto V")
print(video_game_list)
video_game_list.insert(3, "Forza Motorsports")
print(video_game_list)
video_game_list.pop(-1)
print(video_game_list)
video_game_list.reverse()
print(video_game_list)
print(sorted(video_game_list))
