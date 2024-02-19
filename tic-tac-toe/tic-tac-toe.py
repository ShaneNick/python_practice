board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

partially_filled_board = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    ["O", " ", " "]
]

#Checks to see if board is clear 
def intilize_game(board):
    clear_space = []
    for row_index, row in enumerate(board):
        if row == [" ", " ", " "]:
            pass
            for col_index, cell in enumerate(row):
                if cell == " ":
                    clear_space.append((row_index, col_index))

    if clear_space:
        print(f"Board is clear {clear_space}")
        return True, clear_space
    else:
        print("No clear space found")
        return False, []
    
intilize_game(board)

intilize_game(partially_filled_board)

def display_options():
    print("Please choose an option (enter the number):")
    print("1. Row 1")
    print("2. Row 2")
    print("3. Row 3")
    print("4. Exit")

    choice_unclean = input("Your choice: ")
    choice_clean = choice_unclean.strip().lower()
    return choice_clean

choice_clean = display_options()

row_spot = input('Please choose a spot in the row: ')
symbol = input('Please select X or O')




if choice_clean == "row 1":
    print(row_spot)
    if row_spot == 1:
        print(symbol)
        if symbol == 'X' or 'O':
            print("hi")

elif choice_clean == "row 2":
    print('Yes')
elif choice_clean == "row 3":
    print('Yes')
elif choice_clean == "row 4":
    print('Yes')
else:
    print('Invalid row, please choose again')