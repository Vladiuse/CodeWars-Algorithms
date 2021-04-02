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
        dic = {'P': 'W',
               'p': 'B'}
        for line_id, line in enumerate(self.board):
            for s_id, square in enumerate(line):
                if square != '.':
                    new = dic[square]
                    self.board[line_id][s_id] = new

    def move(self, one, two):
        one_line, one_col = self.transtorm(one)
        two_line, two_col = self.transtorm(two)
        self.board[two_line][two_col] = self.board[one_line][one_col]
        self.board[one_line][one_col] = '.'

    def transtorm(self, coors):
        position = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                    'e': 4, 'f': 5, 'g': 6, 'h': 7,
                    }
        col, line = list(coors)
        col = position[col]
        line = 8 - int(line)
        return line, col


starts_board = Board(board)

starts_board.black_while()
print(starts_board)
starts_board.move('a2', 'a4')
print(starts_board)
starts_board.move('h7', 'e1')
print(starts_board)
