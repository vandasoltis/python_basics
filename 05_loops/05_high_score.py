student_scores = input("Input a lists of student scores: ").split()

highest_score = int(student_scores[0]) # I could use 0, but in general to select the largest element, I cant use a default value.

for score in student_scores:
  student_score = int(score)
  if student_score > highest_score:
    highest_score = student_score

print(f"The highest score in the class is: {highest_score}")
