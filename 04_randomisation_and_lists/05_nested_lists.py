#List within a list - nested list

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]


dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
 
#printing the first, then the second list
print(dirty_dozen[0])
print(dirty_dozen[1])

# if: list=[[A,B,C],[E,F,G]], then E = list[1][0]

#printing the third item from the second list
print(dirty_dozen[1][2])

print(dirty_dozen[1][3])

print(dirty_dozen[1][1])