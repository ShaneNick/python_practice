import json

class DictBoard:
    def __init__(self, size=3):
        #initializes tic-tac-toe board
        self.size = size
        self.board = {(x, y): ' ' for x in range(size) for y in range(size)}
        self.game_over = False


        player_symbol = input("Chooese your symbol (X/O): ").upper()
        while player_symbol not in ['X', 'O']:
            print("Invalid Choice. Please select 'X' or 'O'.")
            player_symbol = input("Chooese your symbol (X/O): ").upper()


        self.current_player = player_symbol
        self.ai_player = 'O' if player_symbol == 'X' else 'X'

    def display(self):
        for y in range(self.size):
            print('|'.join(self.board[(x, y)] for x in range(self.size)))
            if y < self.size - 1:
                print('-' * (self.size * 2 - 1))
    
    def make_move(self, x, y, player):
        if self.board[(x,y)] == ' ':
            self.board[(x,y)] = player
            return True
        return False

    def ai_move(self):
        for (x, y), value in self.board.items():
            if value == ' ':
                self.make_move(x, y, self.ai_player)
                break
        self.check_game_status()


    def players_move(self):
        valid_move = False
        while not valid_move:
            row_spot = input('Please choose a row (1, 2, or 3): ')
            col_spot = input('Please select a column (1, 2, or 3): ')
            if row_spot in ['1', '2', '3'] and col_spot in ['1', '2', '3']:
                row, col = int(row_spot) - 1, int(col_spot) - 1
                valid_move = self.make_move(col, row, self.current_player)
                if not valid_move:
                    print("This space is already occupied.")
            else:
                print("Invalid selection. Please choose between 1, 2, or 3 for both row and column.")
        self.check_game_status()

                
                #Checks if move was a winning move thus ending the game 
    def check_game_status(self):
        if self.check_win():
            self.display()
            print(f"Player {self.current_player} wins!")
            self.game_over = True
        elif self.check_draw():
            self.display()
            print("It's a draw!")
            self.game_over = True
        else:
            # Switch players
            self.current_player = 'X' if self.current_player == 'O' else 'O'
            if self.current_player == self.ai_player:
                self.ai_move()
              


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
        # The ai_move method is now called within players_move if necessary

if __name__ == "__main__":
    main()



