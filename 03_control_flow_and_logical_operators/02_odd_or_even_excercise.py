# modulo - is written as a percentage sign and it gives the remainder after a division
# even numbers can be divided by 2 with no remainder
# 6 % 2 = 0
# 5 / 2 = 2 x 2 + 1 , remainder is 1
# therefore: 5 % 2 = 1

number = int(input("Which number do you want to check?"))

number_modulo = number % 2

if number_modulo == 0: 
    print("This is an even number")
else:
    print("This is an odd number")
