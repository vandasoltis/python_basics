print("Type a two digit number:") 
numb = input()

#print(type(numb))
#If I put a two digit number in it, then will be a string type


#Subscripting
first_digit = numb[0]
second_digit = numb[1]

#It has to be an integers data type to work with numbers
print(int(first_digit) + int(second_digit))
