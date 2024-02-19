import json

class DictBoard:
    def __init__(self, size=3):
        #initializes tic-tac-toe board
        self.size = size
        self.board = {(x, y): ' ' for x in range(size) for y in range(size)}

    def display(self):
        for y in range(self.size):
            print('|'.join(self.board[(x, y)] for x in range(self.size)))
            print('-' * (self.size * 2 - 1))

    def players_move(self):
            row_spot = input('Please choose a row (1, 2, or 3): ')
            symbol = input('Please select X or O: ').upper()

            if symbol not in ['X', 'O']:
                print("Invalid symbol. Please select 'X' or 'O'.")
                return

            if row_spot in ['1', '2', '3']:
                placement = input('Please select a column (1, 2, or 3): ')

                if placement in ['1', '2', '3']:
                    # Convert row and column to zero-based index
                    row = int(row_spot) - 1
                    col = int(placement) - 1

                    # Check if the cell is empty before placing the symbol
                    if self.board[(col, row)] == ' ':
                        self.board[(col, row)] = symbol
                        self.display()  # Display the board after the move
                    else:
                        print("This space is already occupied.")
                else:
                    print("Invalid column selection. Please choose between 1, 2, or 3.")
            else:
                print('Invalid row selection. Please choose between 1, 2, or 3.')

    def check_win(self):
    # Check horizontal and vertical lines
        for i in range(self.size):
            if all(self.board[(i, j)] == 'X' for j in range(self.size)) or all(self.board[(i, j)] == 'O' for j in range(self.size)):
                return True
            if all(self.board[(j, i)] == 'X' for j in range(self.size)) or all(self.board[(j, i)] == 'O' for j in range(self.size)):
                return True

        # Check diagonals
        if all(self.board[(i, i)] == 'X' for i in range(self.size)) or all(self.board[(i, i)] == 'O' for i in range(self.size)):
            return True
        if all(self.board[(i, self.size - 1 - i)] == 'X' for i in range(self.size)) or all(self.board[(i, self.size - 1 - i)] == 'O' for i in range(self.size)):
            return True

        return False



board = DictBoard()
board.display()  # Display the initial state of the board
board.players_move()  # Allow the player to make a move and display the updated board
