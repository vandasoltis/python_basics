print("Welcome to the Band Name Generator!")

city = input("Where did you grow up?\n") # Option 1 for new line

print("What is your pet name?") # Option 2 for new line
pet_name = input()

brand_name = city + " " + pet_name # One line should represent one step, so this is better than: print("Your band name is:\n" + city + " " + pet_name)

print("Your band name is:")
print(brand_name)
