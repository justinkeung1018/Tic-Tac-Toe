'''
Write a program that creates tic-tac-toe. 
Write a program that prints a grid like the following one:
||  ||   ||  ||   ||  ||
||  ||   ||  ||   ||  ||
||  ||   ||  ||   ||  ||
Two players play at turns and they have to choose a position in the grid.
The position is chosen using the terminal and each player needs to provide a number,
from 1 to 9. To each number there is a corresponding position in the grid, as follows:
|| 1 ||   || 2 ||   || 3 ||
|| 4 ||   || 5 ||   || 6 ||
|| 7 ||   || 8 ||   || 9 ||
For example, if player 1 (with X), at turn 1 chooses position 1, the grid will look like this:
|| X ||   ||   ||   ||   ||
||   ||   ||   ||   ||   ||
||   ||   ||   ||   ||   ||
Then, if player 2 (with O) chooses position 8, the grid will look like this:
|| X ||   ||   ||   ||   ||
||   ||   ||   ||   ||   ||
||   ||   || O ||   ||   ||
The game ends when one of the two players is able to allign their own marker on three different cells or when 
it is impossible for any player to win
'''

size = int(input("Enter the value of N for a NxN grid: "))
status = [[" " for n in range(size)] for n in range(size)]

# Defining winning conditions
conditions = []
for i in range(size):
    col = [n * size + i for n in range(size)]
    conditions.append(col)

for i in range(size):
    row = [i * size + n for n in range(size)]
    conditions.append(row)

diag1 = [n * (size + 1) for n in range(size)]
conditions.append(diag1)
diag2 = [n * (size - 1) for n in range(1, size + 1)]
conditions.append(diag2)

# Colors
colors = {
    "grid": "\033[97m", # Bright white
    "pos": "\033[90m", # White 
    "X ": "\033[91m", # Bright red
    "O ": "\033[92m", # Bright green
    "end": "\033[0m"
}

# Marks for each player
marks = ["X ", "O "]

# Prints grid
def printGrid():
    for row in range(size):
        outputs = []
        for col in range(size):
            content = status[row][col]
            if content == " ":
                content = f"{row * size + col + 1}"
                if int(content) < 10:
                    content += " "
                outputs.append(f"{colors['grid']}||{colors['end']} {colors['pos']}{content}{colors['end']} ||")
            else:
                outputs.append(f"{colors['grid']}||{colors['end']} {colors[content]}{content}{colors['end']} ||")
        print("   ".join(outputs))

printGrid()

# 1. Check if grid position is already taken
# 2. If not, place X or O
# 3. Check if game ends (a. someone wins, b. nobody wins)
# 4. If not, repeat steps 1 to 3

# Additional error checking:
# 1. Input is beyond 1 to 9
# 2. Input is not an integer

# Iterations
# 1. NxN board
# 2. Colored grids
# 3. Numbered grids

while True:
    for n in [0, 1]:
        pos = int(input(f"Player {n+1}, enter a position from 1 to {size ** 2}: ")) - 1

        # Checks if position is out of range
        while pos < 0 or pos > size ** 2 - 1:
            pos = int(input(f"Error: invalid input, enter another position from 1 to {size ** 2}: ")) - 1
        
        # Checks if grid position is already taken
        while status[pos // size][pos % size] != " ":
            pos = int(input(f"Error: position already taken, enter another position from 1 to {size ** 2}: ")) - 1

        # Places mark
        status[pos // size][pos % size] = marks[n]
        
        # Prints NxN grid
        printGrid()

        # Checks if somebody wins
        player_marks = []
        for line in range(size):
            line_marks = [i + line * size for i, x in enumerate(status[line]) if x == marks[n]]
            player_marks += line_marks

        for condition in conditions:
            if set(condition).issubset(player_marks):
                print(f"Game over. Player {n + 1} wins!")
                quit()
        
        # Nobody wins
        if not any(" " in line for line in status):
            print("Game over. Nobody wins!")
            quit()