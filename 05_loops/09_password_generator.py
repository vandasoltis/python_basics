import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_len = len(letters)
numbers_len = len(numbers)
symbols_len = len(symbols)

print("Welcome to the Password Generator!")
letters_count = int(input("How many letters would you like in your password?\n")) 
numbers_count = int(input(f"How many numbers would you like?\n"))
symbols_count = int(input(f"How many symbols would you like?\n"))

password_characters = []

for _count in range(letters_count):
  random_choice = random.randint(0, letters_len - 1)
  letter = letters[random_choice]
  password_characters += letter

for _count in range(numbers_count):
  random_choice = random.randint(0, numbers_len - 1)
  number = numbers[random_choice]
  password_characters += number

for _count in range(symbols_count):
  random_choice = random.randint(0, symbols_len - 1)
  symbol = symbols[random_choice]
  password_characters += symbol

random.shuffle(password_characters)

password = ""
for character in password_characters:
  password += character

print(password)
