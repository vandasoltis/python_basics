print("Enter your height in m:")
height_input = input() 

print("Enter your weight in kg:")
weight_input = input()

height = float(height_input)
weight = int(weight_input)

bmi = weight / height ** 2

bmi_rounded = round(bmi)

if bmi < 18.5: 
  print(f"Your BMI is {bmi_rounded}, you are underweight")
elif bmi <= 25: 
  print(f"Your BMI is {bmi_rounded}, you have a normal weight")
elif bmi <= 30: 
  print(f"Your BMI is {bmi_rounded}, you are slightly overeight")
elif bmi <= 35: 
  print(f"Your BMI is {bmi_rounded}, you are obese")
else:
  print(f"Your BMI is {bmi_rounded}, you are clinically obese")
