row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

user_input = input("What position do you want to put the treasure? (e.g.: 1,2): ")
positions = user_input.split(",")

column = positions[0] #can be also X or horizontal
row = positions[1] #can be also Y or vertical

column_index = int(column) - 1
row_index = int(row) - 1

map[row_index][column_index] = 'X'

print(f"{row1}\n{row2}\n{row3}")
