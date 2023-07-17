#For Loop
for i in [1, 2, 3, 4, 5]:
  print("I am inside the loop five times")
print("I am outside the loop")

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits: 
    print(fruit)
    print(fruit + " Pie")
print(fruits)

#Another solution

# fruits[0] with use of index: i iterating in range of the length of fruits
# fruits[1]
# fruits[2]

fruits = ["Apple", "Peach", "Pear"]
number_of_fruits = len(fruits)
for i in range(0, number_of_fruits): 
    print(fruits[i])
    print(fruits[i] + " Pie")
print(fruits)

for i in range(0, 100):
  print(f"I am inside the loop {i+1}/100 times") #i = 0, 1, 2..... 97, 98, 99
print("I am outside the loop")
