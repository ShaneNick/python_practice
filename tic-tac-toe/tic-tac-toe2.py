import json

class DictBoard:
    def __init__(self, size=3):
        #initializes tic-tac-toe board
        self.size = size
        self.board = {(x, y): ' ' for x in range(size) for y in range(size)}
        self.current_player = 'X'
        self.game_over = False
        self.ai_player = 'O'

    def display(self):
        for y in range(self.size):
            print('|'.join(self.board[(x, y)] for x in range(self.size)))
            print('-' * (self.size * 2 - 1))
    
    def ai_move(self):
        for (x, y), value in self.board.items():
            if value == ' ':
                self.board[(x, y)] = self.ai_player
                break
        self.current_player = 'X'


        # Inside players_move and ai_move, after making a move:
        if self.check_win():
            # Announce win based on the last move made, not current_player
            print(f"Player {'X' if self.current_player == 'O' else 'O'} wins!")  # Assumes last move was winning
            self.game_over = True
        elif self.check_draw():
            print("It's a draw!")
            self.game_over = True



    def players_move(self):
            #Players selection to put their piece 
            if self.current_player != self.ai_player:
                valid_move = False
                while not valid_move:
                    row_spot = input('Please choose a row (1, 2, or 3): ')
                    #symbol = input('Please select X or O: ').upper()

                    # if symbol not in ['X', 'O']:
                    #     print("Invalid symbol. Please select 'X' or 'O'.")
                    #     return

                    if row_spot in ['1', '2', '3']:
                        placement = input('Please select a column (1, 2, or 3): ')

                        if placement in ['1', '2', '3']:
                            # Convert row and column to zero-based index
                            row = int(row_spot) - 1
                            col = int(placement) - 1

                            # Check if the cell is empty before placing the symbol
                            if self.board[(col, row)] == ' ':
                                #self.board[(col, row)] = symbol
                                self.board[(col, row)] = self.current_player
                                valid_move = True
                           
                                
                            else:
                                print("This space is already occupied.")
                        else:
                            print("Invalid column selection. Please choose between 1, 2, or 3.")
                    else:
                        print('Invalid row selection. Please choose between 1, 2, or 3.')
                    valid_move = True

                #Switches to ai after human valid move
                    self.current_player = self.ai_player
                    self.ai_move()

                
                #Checks if move was a winning move thus ending the game 
    def check_game_status(self):
                if self.check_win():
                    print(f"Player {self.current_player} wins!")
                    self.game_over = True
                    return
                #Or checks to see if move caused a draw
                elif self.check_draw():
                    print("It's a draw!")
                    self.game_over = True
                else:
                    if self.current_player == self.ai_player:
                        self.current_player = 'X' 
                
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    

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

    def check_draw(self):
        for cell in self.board.values():
            if cell == ' ':
                return False
        return True
        

def main():
    game = DictBoard()
    while not game.game_over:
        game.display()
        if game.current_player != game.ai_player:
            game.players_move()
      

if __name__ == "__main__":
    main()



