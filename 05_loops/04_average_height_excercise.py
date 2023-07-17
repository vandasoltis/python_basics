student_heights = input("Input a lists of student heights: ").split() # Getting the input

# To calculate avarage height, we need to know how many students we have, and what is the sum of their heights, then divide total_height with total_number

# Calculating total_height, adding each height of the students to the total, wich is initially set to 0 before the loop:
total_height = 0

for height in student_heights:
  student_height = int(height)
  total_height = total_height + student_height


# Calculating len(student_heights), counting the elements, adding 1 to total in each iteration of the loop:
total_number = 0

for height in student_heights:
  total_number = total_number + 1 #Each time there is a height, we need to add 1 to the total number

avarage_height = total_height / total_number

print("Solution #1:")
print(avarage_height)


# This two for loops can be merged and provide the same results:
total_height = 0
total_number = 0
for height in student_heights:
  student_height = int(height)
  total_height = total_height + student_height
  total_number = total_number + 1

avarage_height = total_height / total_number

print("Solution #2:")
print(avarage_height)
