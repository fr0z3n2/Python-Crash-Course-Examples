# 5-1
selected_menu_item = 'hamburger';
print("Did you select hamburger? I predict true.");
print(selected_menu_item == 'hamburger')

print("Did you select cheeseburger? I predict false.")
print(selected_menu_item == 'cheeseburger')

menu_items = ['cake', 'hamburger', 'steak', 'fried oysters']

if (selected_menu_item in menu_items):
	print("Sure! I'll take your order")
else:
	print("Sorry bub! Order something else")

# 5-2
item1 = 'subaru'
item2 = 'toyota'
print(item1.upper() == 'subaru' or item1.lower() == 'subaru')

# I have seen this so much, but essentially this is how to do it in Python3

