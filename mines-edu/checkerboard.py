print("How many rows does the checkerboard have?")
rows = int(input("ROWS> "))
print("How many columns does the checkerboard have?")
columns = int(input("COLUMNS> "))
print("What are the strings with which to pattern it?")
first = str(input("FIRST> "))
second = str(input("SECOND> "))

print(f"A checkboard with: {rows} rows, {columns} columns, first string is {first}, and second string is {second}; is:")

board = []
currentRow = []
currentString = first

for i in range(rows):
    for j in range(columns):
        
        if j > 0:
            if currentString == first:
                currentString = second
            elif currentString == second:
                currentString = first
        else:
            if columns % 2 != 0:
                if currentString == first:
                    currentString = second
                elif currentString == second:
                    currentString = first
        currentRow.append(currentString)
    print(f"OUTPUT {currentRow}")
    board.append(currentRow.copy())
    currentRow.clear()

print("And the 2D array representation is:")
print(f"OUTPUT {board}")
