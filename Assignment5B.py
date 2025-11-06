
import random

numberOfUndiscoveredTreasures = 0
board = []
w = int(input("Enter the width of the grid: "))
h = int(input("Enter the height of the grid: "))
for i in range(h):
    row = []
    for j in range(w):
        chance = random.random()
        if chance >= 0.7:
            row.append("T")
            numberOfUndiscoveredTreasures += 1
        else:
            row.append("O")
    board.append(row)
emptyboard = []
for i in range(h):
    row = []
    for j in range(w):
        row.append("O")
    emptyboard.append(row)
print(f"Number of treasures hidden: {numberOfUndiscoveredTreasures}")
while numberOfUndiscoveredTreasures > 0:
    rowguess = int(input(f"Enter the row number (0 to {w - 1}): "))
    colguess = int(input(f"Enter the column number (0 to {h - 1}): "))
    if board[rowguess][colguess] == "T":
        numberOfUndiscoveredTreasures -= 1
        emptyboard[rowguess][colguess] = "X"
        board[rowguess][colguess] = "X"
        print("Congratulations! You found a treasure!")
        for row in emptyboard:
            print("".join(row))
    else:
        print("No treasure here, try again!")
print("Congratulations! You've found all the treasures!")
for row in emptyboard:
    print("".join(row))


