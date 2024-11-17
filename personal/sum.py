import re

regex = r"(\d*\,)?\d+"

sum = 0

with open('input.txt') as weights_file:
    for line in weights_file:
        match = re.search(regex, line)[0]
        number = float(match.replace(',','.'))
        print(f"{line} found number: {number}")  
        sum += number

print("--------------------------------")
print("--------------------------------")
print(f"Sum: {sum}")
