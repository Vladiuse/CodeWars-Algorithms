# info = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
#         ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
#         ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
#         ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
#         ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
#         ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
#         ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
#         ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]

board = [[".", ".", ".", ".", ".", ".", ".", "."],
         ["p", "p", "p", "p", "p", "p", "p", "p"],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         ["P", "P", "P", "P", "P", "P", "P", "P"],
         [".", ".", ".", ".", ".", ".", ".", "."]

         ]
# P in while p is black
move = ["e4", "d5", "d3", "dxe4"]


class Board:

    def __init__(self, board):
        self.board = board

    def __str__(self):
        rez = ''
        number = 8
        alpha = '  a b c d e f g h\n'
        for line in self.board:
            line = line.copy()
            line.insert(0, str(number))
            number -= 1
            line = ' '.join(line)
            rez += line + '\n'
        return rez + alpha

    def black_while(self):
        # it not because i'm racist!
        dic = {'P': 'W',
               'p': 'B'}
        for line_id, line in enumerate(self.board):
            for s_id, square in enumerate(line):
                if square != '.':
                    new = dic[square]
                    self.board[line_id][s_id] = new

    def move(self, one, two):
        one_line, one_col = self._transtorm(one)
        two_line, two_col = self._transtorm(two)
        self.board[two_line][two_col] = self.board[one_line][one_col]
        self.board[one_line][one_col] = '.'

    def _transtorm(self, coors):
        position = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                    'e': 4, 'f': 5, 'g': 6, 'h': 7,
                    }
        col, line = list(coors)
        col = position[col]
        line = 8 - int(line)
        return line, col

    def _transtorm_to_chess(self, line, col):
        position = {0: 'a', 1: 'b', 2: 'c', 3: 'd',
                    4: 'e', 5: 'f', 6: 'g', 7: 'h',
                    }
        col = position[col]
        line = 8 - int(line)
        return str(col) + str(line)

    def _is_figure(self, coors):
        line, col = self._transtorm(coors)
        return self.board[line][col] != '.'

    def get_square(self, line, col):
        return self.board[line][col]


class Player:
    chess = {'white': 'P',
             'black': 'p'}

    def __init__(self, color, board, figure):
        self.color = color
        self.board = board
        self.figure = figure

    def move_type(self, move):
        if 'dx' in move:
            return 'kill'
        return 'move'

    def decision(self, move):
        if self.move_type(move) == 'move':
            move_from = self.coor_from_move(move)
            self.board.move(move_from, move)

    def coor_from_move(self, move):
        player_direction = {'white': 1,
                            'black': -1}
        line, col = self.board._transtorm(move)
        line = line + player_direction[self.color]
        if self.board.get_square(line, col) == self.figure:
            return self.board._transtorm_to_chess(line, col)


def move_queue(moves):
    try:
        for i in range(0, len(moves), 2):
            yield moves[i], moves[i + 1]
    except IndexError:
        yield moves[-1], None


my_board = Board(board)
print(my_board)
white_player = Player(color='white', board=my_board, figure='P')
black_player = Player(color='black', board=my_board, figure='p')

move_line = ['a3', 'a6', 'b3', 'b6', 'c3', 'c6', 'f3', 'f6', ]
for move in move_queue(move_line):
    white_move = move[0]
    black_move = move[1]
    white_player.decision(white_move)
    black_player.decision(black_move)
    print(my_board)
