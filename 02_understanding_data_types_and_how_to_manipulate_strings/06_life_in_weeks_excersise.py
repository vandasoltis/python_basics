#how many days, weeks, months we have left if we live until 90 years old?

#Solution 1

print("What is your current age?")
age = input() 

current_age_day = 365 * int(age)
current_age_week = 52 * int(age)
current_age_month = 12 * int(age)

age_90_day = 365 * 90 
age_90_week = 52 * 90
age_90_month = 12 * 90

day = age_90_day - current_age_day
week = age_90_week - current_age_week
month = age_90_month - current_age_month

message = f"You have {day} days, {week} weeks, and {month} months left"
print(message)

#Solution 2

print("What is your current age?")
age = input() 

age_as_int = int(age)

years_reamining = 90 - age_as_int
days_reamining = years_reamining * 365
weeks_reamining = years_reamining * 52
months_reamining = years_reamining * 12

message = f"You have {days_reamining} days, {weeks_reamining} weeks, and {months_reamining} months left"
print(message)