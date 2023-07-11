print("Enter your height in m:")
height_input = input() #1.61

print("Enter your weight in kg:")
weight_input = input() #55

# print(type(height_input)) #<class 'str'>
# print(type(weight_input)) #<class 'str'>

height = float(height_input)
weight = int(weight_input)
# BMI = kg / m**2

bmi = weight / height ** 2

# print(bmi) # 21.218317194552675

# print(type(bmi)) # <class 'float'>

bmi_int = int(bmi)

print(bmi_int) # 21
