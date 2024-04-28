from player import humanplayer , randomcomputerplayer
class tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row) + '|')
            
    @staticmethod
    def print_borad_nums():
        number_board = [[str(i) for i in range(j+3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row) + '|')
    def avaiable_move(self):
        moves=[]
        for(i,x) in enumerate(self.board):
            if x == ' ':
                moves.append(i)
        return moves
    def empty_squares(self):
        return ' 'in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] =='':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #check rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            if row.count(letter) == 3:
                return True
        #check columns
        for i in range(3):
            if self.board[i] == letter and self.board[i+3] == letter and self.board[i+6] == letter:
                return True
        #check diagonals
        if self.board[0] == letter and self.board[4] == letter and self.board[8] == letter:
            return True
        if self.board[2] == letter and self.board[4] == letter and self.board[6] == letter:
            return True
        return False
def play(game, x_player , o_player, print_game=True):
    if print_game:
        game.print_borad_nums()
        
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square ' + str(square))
                game.print_board()
                print(' ')
            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter
                
            letter = 'O' if letter == 'X' else 'X'
            
        if print_game:
            print('tie')
if __name__ == '__main__':
    x_player = humanplayer('X')
    o_player = randomcomputerplayer('O')
    game = tictactoe()
    play(game, x_player, o_player, print_game=True)