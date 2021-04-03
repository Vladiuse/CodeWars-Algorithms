class IncorrectMove(BaseException):

    def __init__(self, txt, info='no info'):
        self.info = info
        self.txt = f'{txt} is invalid'


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
        if len(move) == 2:
            return 'move'
        if len(move) == 4 and move[:2] == 'dx':
            return 'kill'
        else:
            raise IncorrectMove(txt=move, info=f'некоректный вод {move}')

    def decision(self, move):
        if self.move_type(move) == 'move':
            move_from = self.coor_from_move(move)
            self.board.move(move_from, move)
        else:
            beat_from = self.beat(move)
            self.board.move(beat_from, move[2:])

    def coor_from_move(self, move):
        player_direction = {'white': 1,
                            'black': -1}
        p_double_move = {'white': '4',
                         'black': '5'}
        line, col = self.board._transtorm(move)
        line = line + player_direction[self.color]
        if self.board.get_square(line, col) == self.figure:  # проверка на один назад
            return self.board._transtorm_to_chess(line, col)
        else:
            # пробуей пойти на 2 клетки
            if p_double_move[self.color] == move[1]:
                line = line + player_direction[self.color]
                if self.board.get_square(line, col) == self.figure:
                    return self.board._transtorm_to_chess(line, col)

            else:
                raise IncorrectMove(txt=move, info=f'на 2 клетки сюда нельзя ходить {move}')

    def beat(self, move):
        start_move = move
        player_direction = {'white': 1,
                            'black': -1}
        move = move[2:]
        line, col = self.board._transtorm(move)
        to_beat = self.board.get_square(line, col)
        if to_beat != '.' and to_beat != self.figure:
            line = line + player_direction[self.color]
            cols = [col - 1, col + 1]
            for id, c in enumerate(cols):
                if c < 0 or c > 7:
                    cols[id] = None
                else:
                    if self.board.get_square(line, c) == self.figure:  # если есть наша фигура чтобы побить
                        pass
                    else:
                        cols[id] = None
            if any(cols):
                cols.remove(None)
                for c in cols:  # расчитываем что фигура чтобы побить только одна
                    beat_from = self.board._transtorm_to_chess(line, c)
                    return beat_from
            else:
                raise IncorrectMove(txt=start_move, info=f'нет фигуры чтобы побить dx{start_move}')


        else:
            raise IncorrectMove(txt=start_move, info='нельзя побить пустоту или свою фигуру')


def move_queue(moves):
    try:
        for i in range(0, len(moves), 2):
            yield moves[i], moves[i + 1]
    except IndexError:
        yield moves[-1], None


def pawn_move_tracker(moves):
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]

    my_board = Board(board)
    white_player = Player(color='white', board=my_board, figure='P')
    black_player = Player(color='black', board=my_board, figure='p')

    move_line = moves
    # move_line = ['d4', 'd5', 'e4', 'e5', 'dxd5', 'dxd4', 'a4', 'c6', 'dxc6', 'dxc6', 'dxc6']
    try:
        for move in move_queue(move_line):
            white_move = move[0]
            black_move = move[1]
            white_player.decision(white_move)
            if black_move:
                black_player.decision(black_move)
        return my_board.board
    except IncorrectMove as exc:
        return exc.txt


print(pawn_move_tracker(["dxe3", "d6", "e4", "a6"]))

mov_1 = ['a4', 'a5', 'b4', 'b5', 'c4', 'b4']
# should equal 'b4 is invalid'
mov_2 = ['h3', 'h5', 'h4', 'g5', 'hxg5', 'h4']
rez = [['.', '.', '.', '.', '.', '.', '.', '.'], ['p', 'p', 'p', 'p', 'p', 'p', '.', '.'],
       ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', 'P', '.'],
       ['.', '.', '.', '.', '.', '.', '.', 'p'], ['.', '.', '.', '.', '.', '.', '.', '.'],
       ['P', 'P', 'P', 'P', 'P', 'P', 'P', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]

mov_3 = ['a3', 'h6', 'a4', 'h5', 'a5', 'h4', 'a6', 'h3', 'axb7', 'hxg2']
