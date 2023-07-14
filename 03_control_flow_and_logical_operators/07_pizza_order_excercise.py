# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

#first solution

print("Welcome to the Python Pizza Deliveries!")     
size = input("What size pizza do you want? S, M or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
  bill += 15
  if pepperoni == "Y":
    bill += 2

if size == "M":
  bill += 20
  if pepperoni == "Y":
    bill += 3

if size == "L":
  bill += 25
  if pepperoni == "Y":
    bill += 3

if cheese == "Y":
  bill += 1


print(f"Your final bill is ${bill}.")     


#  second solution

print("Welcome to the Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if pepperoni == "Y":
  if size == "S":
    bill +=2
  else:
    bill+=3

if cheese == "Y":
  bill +=1

print(f"Your final bill is: ${bill}.")   
