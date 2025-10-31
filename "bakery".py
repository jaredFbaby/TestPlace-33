

print("Boudreaux & Thibodeaux's Bakery")
print("-------------------------------")
print("1. Muffin: $5.95")
print("2. King Cake Slice: $4.95")
print("3. Croissant: $3.95")
print("4. Scone: 3.75")

menu= [ 1, 2, 3, 4]
price=[5.95, 4.95, 3.95, 3.75]
choicePrice=0
choice=input("What would you like to order? Type the appropriate number of the menu item.")

while choice not in menu:
    choice = input("Invalid choice. Type the appropriate number of the menu item. or DONE when order is completed.")



