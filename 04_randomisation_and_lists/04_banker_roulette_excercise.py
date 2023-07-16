#https://docs.python.org/3/tutorial/datastructures.html
#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random

#First solution

names_string = input("Give me everybody's name, seperated by a comma. ")
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]


print(person_who_will_pay + " is going to buy the meal today!") 


#Second solution

names_string = input("Give me everybody's name, seperated by a comma. ")
names = names_string.split(", ")

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!") 
