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
# 4. N players

size = int(input("Enter the value of N for a NxN grid: "))
players = int(input("Enter the number of players: "))

# Colors
system_colors = {
    "grid": "\033[97m", # Bright white
    "pos": "\033[90m", # White 
    "end": "\033[0m"
}

available_colors = {
"red": "\033[91m",
"green": "\033[92m",
"yellow": "\033[93m",
"blue": "\033[94m",
"magenta": "\033[95m",
"cyan": "\033[96m"
}

print("Available colors: \033[91mred\033[0m, \033[92mgreen\033[0m, \033[93myellow\033[0m, \033[94mblue\033[0m, \033[95mmagenta\033[0m, \033[96mcyan\033[0m")

# Marks for each player
marks = {}

# Function for picking mark
def pickMark(n):
    mark = input(f"Player {n + 1}, enter a letter or symbol for your mark: ") + " "
    while True:
        if len(mark) == 2:
            marks[n] = mark
            break
        else:
            mark = input(f"Player {n + 1}, enter ONE letter or symbol: ") + " "

# Function for picking color
def pickColor(n):
    color = input(f"Player {n + 1}, pick a color: ").lower()
    while True:
        try:
            system_colors[n] = available_colors[color]
            break
        except KeyError:
            color = input(f"Player {n + 1}, pick a color FROM THE LIST: ").lower()

def changeMark(n):
    color = system_colors[n]
    del system_colors[n]
    pickMark(n)
    system_colors[n] = color
    
# Players design their own marks
for n in range(players):
    while True:
        pickMark(n)
        pickColor(n)

        # Checks if the new player has chosen a mark-color combination that has already been chosen by another player
        combinations = set()
        for num, mark in marks.items():
            color = system_colors[num]
            combinations.add((mark, color))
        if len(combinations) != n + 1:
            print("Sorry, your combination of mark and color has already been taken. Try again.")
            continue
        break

    while True:
        print(f"Player {n + 1}, this is your mark: {system_colors[n]}{marks[n]}{system_colors['end']}")
        cont = input("Press enter to confirm, enter 1 to change symbol, enter 2 to change color: ")
        if cont == str(1):
            changeMark(n)
        if cont == str(2):
            pickColor(n)
        if not cont:
            break
        else:
            continue

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
                outputs.append(f"{system_colors['grid']}||{system_colors['end']} {system_colors['pos']}{content}{system_colors['end']} ||")
            else:
                outputs.append(f"{system_colors['grid']}||{system_colors['end']} {content}{system_colors['end']} ||")
        print("   ".join(outputs))

printGrid()

while True:
    for n in range(players):
        while True:
            try:
                pos = int(input(f"Player {n + 1}, enter a position from 1 to {size ** 2}: ")) - 1
                break
            except ValueError:
                print()

        # Checks if position is out of range
        while pos < 0 or pos > size ** 2 - 1:
            pos = int(input(f"Error: invalid input, enter another position from 1 to {size ** 2}: ")) - 1
        
        # Checks if grid position is already taken
        while status[pos // size][pos % size] != " ":
            pos = int(input(f"Error: position already taken, enter another position from 1 to {size ** 2}: ")) - 1

        # Places mark
        status[pos // size][pos % size] = system_colors[n] + marks[n]
        
        # Prints NxN grid
        printGrid()

        # Checks if somebody wins
        player_marks = []
        for line in range(size):
            line_marks = [i + line * size for i, x in enumerate(status[line]) if x == system_colors[n] + marks[n]]
            player_marks += line_marks

        for condition in conditions:
            if set(condition).issubset(player_marks):
                print(f"Game over. Player {n + 1} wins!")
                quit()
        
        # Nobody wins
        if not any(" " in line for line in status):
            print("Game over. Nobody wins!")
            quit()