print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is your name?\n")

names_combined = name1 + name2
names_combined_lower = names_combined.lower()

count_true_t = names_combined_lower.count('t')
count_true_r = names_combined_lower.count('r')
count_true_u = names_combined_lower.count('u')
count_true_e = names_combined_lower.count('e')

count_love_l = names_combined_lower.count('l')
count_love_o = names_combined_lower.count('o')
count_love_v = names_combined_lower.count('v')
count_love_e = names_combined_lower.count('e')

true_amount = count_true_t + count_true_r + count_true_u + count_true_e
love_amount = count_love_l + count_love_o + count_love_v + count_love_e

love_score = str(true_amount) + str(love_amount)
love_score_int = int(love_score)

if love_score_int < 10 or love_score_int > 90:
  print(f"Your score is {love_score_int}, you go together like coke and menthos.")
elif love_score_int >= 40 and love_score_int <= 50:
  print(f"Your score is {love_score_int}, you are alright together.")
else:
  print(f"Your score is {love_score_int}.")
