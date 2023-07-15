#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
#this is a module
import random

#Generating random whole numbers
random_integer = random.randint(1,10)
print(random_integer)

#Generating random floating point numbers
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")
