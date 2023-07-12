print("Welcomte to the tip calculator!")

print("What was the total bill?")
total_bill = input("$")

total_bill_as_float = float(total_bill)

#print(type(total_bill_as_float))

print("What percentage would you like to give? 10, 12 or 15?")
tip = input()

tip_as_int = int(tip)

#Converting from percentage
tip_percent = tip_as_int / 100
#print(type(tip_percent))

print("How many people to split the bill?")
people = input()

people_as_int = int(people)

final_payment = ((total_bill_as_float * tip_percent + total_bill_as_float) / people_as_int)
#print(round(final_payment, 2))

final_payment_rounded = round(final_payment, 2)

message = f"Each pearson should pay ${final_payment_rounded}"
print(message)
