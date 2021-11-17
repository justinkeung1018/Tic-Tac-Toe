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

pos1 = ""
pos2 = ""
pos3 = ""
pos4 = ""
pos5 = ""
pos6 = ""
pos7 = ""
pos8 = ""
pos9 = ""

status = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
marks = ["X", "O"]

# Print grid

# 1. Check if grid position is already taken
# 2. If not, place X or O
# 3. Check if game ends (a. someone wins, b. nobody wins)
# 4. If not, repeat steps 1 to 3

# Additional error checking:
# 1. Input is beyond 1 to 9
# 2. Input is not an integer

while True:
    for n in [0, 1]:
        pos = int(input(f"Player {n+1}, enter a position from 1 to 9: ")) - 1

    # Checks if grid position is already taken
        while status[pos] != " ":
            pos = int(input("Error: position already taken, enter another position from 1 to 9: ")) - 1

        # Places mark
        status[pos] = marks[n]
        
        # Prints grid
        print(f"|| {status[0]} ||   || {status[1]} ||   || {status[2]} ||\n|| {status[3]} ||   || {status[4]} ||   || {status[5]} ||\n|| {status[6]} ||   || {status[7]} ||   || {status[8]} ||")

        # Checks if somebody wins
        player_marks = [i for i, x in enumerate(status) if x == marks[n]]

        col1 = [0, 3, 6]
        col2 = [1, 4, 7]
        col3 = [2, 5, 8]
        row1 = [0, 1, 2]
        row2 = [3, 4, 5]
        row3 = [6, 7, 8]
        diag_left = [0, 4, 8]
        diag_right = [2, 4, 6]
        game_ends = [col1, col2, col3, row1, row2, row3, diag_left, diag_right]
        
        for condition in game_ends:
            if set(condition).issubset(player_marks):
                print(f"Game over. Player {n+1} wins!")
                quit()
        
        # Nobody wins
        if " " not in status:
            print("Game over. Nobody wins!")
            quit()
        


