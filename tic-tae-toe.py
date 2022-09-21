#Tiki Taka Toe game develop by Kevin Salas
#Creating the grid lines


grid = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]
def main():
    print("Tiki-Taka-Toe game (to avoid copyright) game develop by Kevin Salas")
    player = change_turns("")
    while not (winner(grid) or draw(grid)):
        game(grid)
        player_turns(player, grid)
        player = change_turns(player)
    game(grid)
    print("Good Game")
# Making the board to play    
def game(grid):
    print(grid[0] + "|" + grid[1] + "|" + grid[2])
    print("-+-+-")
    print(grid[3] + "|" + grid[4] + "|" + grid[5])
    print("-+-+-")
    print(grid[6] + "|" + grid[7] + "|" + grid[8])

def player_turns(player,grid):
    turn = int(input(f"{player}'s turn select a number (1-9): "))
    grid[turn - 1] = player
    # while grid[turn] == "x" or grid[turn] == "o":
    #     print("stop, you're violating the law.")
    #     turn = int(input(f"{player}'s turn select a number (1-9): "))
        
    
def winner(grid):
    return (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6])

def draw(grid):
    for draw in range(9):
        if grid[draw] != "x" and grid[draw] != "o":
            return False
    return True
def change_turns(current_player):
    if current_player == "" or current_player == "x":
        return "o"
    elif current_player == "o":
        return "x"
    
if __name__ == "__main__":
    main()