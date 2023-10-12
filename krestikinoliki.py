from tkinter import *

# root = Tk()


CANVAS_SIZE = 600
FIGURE_SIZE = 200
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None
O = "player 1"
X = "player 2"
FIRST_PLAYER = X

# can = Canvas(root, width=600, height=600)
# can.pack()


class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.game_status = True
        self.current_player = start_player
        self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY],
        ]    

    def bg(self, grid_color):
        self.canvas.create_line(200, 0, 200, 600, fill=grid_color)
        self.canvas.create_line(400, 0, 400, 600, fill=grid_color)
        self.canvas.create_line(0, 200, 600, 200, fill=grid_color)
        self.canvas.create_line(0, 400, 600, 400, fill=grid_color)

    def re_x(self, posX, posY):
        self.canvas.create_line(posX, posY, posX + 200, posY + 200, fill='red', width=3)
        self.canvas.create_line(posX + 200, posY, posX, posY + 200, fill='red', width=3)

    def re_o(self, posX, posY): 
        self.canvas.create_oval(posX + 5, posY + 5, posX + 195, posY + 195, outline='blue', width=3)

    def winner(self, player=None):
        self.game_status = False
        center = 300
        if player:
            text = f'Winner - {player}'
        else:
            text = 'Draw' 
        self.canvas.create_text(300, 300, text=text, fill='grey', font='Arial 50')
        self.canvas.unbind('<Button-1>')

    def click_event(self, event):
        x_coord = event.x // FIGURE_SIZE
        y_coord = event.y // FIGURE_SIZE
        self.make_move(x_coord, y_coord)

        if self.game_status:
            self.ai_best_move()

    def make_move(self, x, y):
        position = {0:0, 1: 200, 2: 400}
        if self.board[x][y] == EMPTY:
            self.update_board(x, y)

            if self.current_player == X:
                self.re_x(position[x], position[y])
            elif self.current_player == O:
                self.re_o(position[x], position[y])
            self.change_player()

    def update_board(self, x, y):
        self.board[x][y] = self.current_player
        if self.check_win(self.board, self.current_player):
            self.winner(self.current_player)
        elif self.check_draw(self.board):
            self.winner()
        print (self.board)

    def check_win(self, board, player):
        for y in range(3):
            if board[y] == [player, player, player]:
                return True
            
        for x in range(3):
            if board[0][x] == board[1][x] == board[2][x] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False
    
    def check_draw(self, board):
        for row in board:
            if EMPTY in row:
                return False
        return True
    
    def change_player(self):
        if self.current_player == X:
            self.current_player = O
        else:
            self.current_player = X

    def minimaks(self, board, isMax):
        board_len = range(len(self.board))

        if self.check_win(board, O):
            return 1
        if self.check_win(board, X):
            return -1
        if self.check_draw(board):
            return 0


        if isMax:
            best_score = float('-inf')
            for i in board_len:
                for g in board_len:
                    if board[i][g] == EMPTY:
                        board[i][g] = O
                        score = self.minimaks(board, False)
                        board[i][g] = EMPTY
                        best_score = max(score, best_score)
        else:
            best_score = float('inf')
            for i in board_len:
                for g in board_len:
                    if board[i][g] == EMPTY:
                        board[i][g] = X
                        score = self.minimaks(board, True)
                        board[i][g] = EMPTY
                        best_score = min(score, best_score)
        return best_score
    
    def ai_best_move(self):
        best_score = float('-inf')
        board_len = range(len(self.board))
        board = self.board[:]
        for i in board_len:
            for g in board_len:
                if board[i][g] == EMPTY:
                    board[i][g] = O
                    score = self.minimaks(board, False)
                    board[i][g] = EMPTY
                    if score > best_score:
                        best_score = score
                        move = i, g

        self.make_move(move[0], move[1])

game1 = Board(start_player=FIRST_PLAYER)

# root = Board()
game1.bg('white')
# game1.winner(player = O)
# game1.re_x(0, 0)
# game1.re_o(0, 0)
game1.title('Крестики нолики')
game1.mainloop()