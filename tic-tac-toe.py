class Board:
    value_cache = {}
    def __init__(self):
        self.board = [[' ' for col in range(3)] for row in range(3)]

    def __str__(self):
        board = ''
        for row in self.board:
            board += "|".join(row) + '\n'
        return board

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def is_finished(self):
        return self.check_three_same() is not None or self.is_full()

    def is_full(self):
        for row in self.board:
            for i in row:
                if i == ' ':
                    return False
        return True

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.get_player()
            return True
        else:
            return False

    def get_player(self):
        turns = 0
        for r in self.board:
            for i in r:
                if i != ' ':
                    turns += 1
        return 'X' if turns%2 == 0 else 'O'

    def get_value(self):
        winner = self.check_three_same()
        if winner:
            if winner == 'X':
                return 1
            else:
                return -1
        elif self.is_full():
            return 0
        else:
            s = str(self)
            if s in self.value_cache:
                print 'getting cached value!!!'
                return self.value_cache[s]
            else:
                boards = self.get_boards()
                values = [child.get_value() for child in boards]
                value = max(values) if self.get_player() == 'X' else min(values)
                self.value_cache[s] = value
                return value

    def get_first_blank_space(self):
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                if self.board[r][c] == ' ':
                    return r, c
        raise ValueError("no moves left")

    def get_best_move(self):
        moves = self.get_moves()
        key = lambda m: moves[m].get_value()
        return max(moves, key=key) if self.get_player() == 'X' else min(moves, key=key)

    def get_moves(self):
        moves = {}
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == ' ':
                    child = Board()
                    child.set_board([r[:] for r in self.board])
                    child.make_move(row, col)
                    moves[row, col] = child
        return moves

    def get_boards(self):
        return self.get_moves().values()

    def three_same(self, ls):
        a, b, c = ls
        if a == b and b == c:
            if a == ' ':
                return None
            else:
                return a
        else:
            return None

    def check_three_same(self):
        size = len(self.board)
        size_range = range(size)

        successful_player = None
        for row in self.board:
            successful_player = successful_player or self.three_same(row)
        for col in size_range:
            successful_player = successful_player or self.three_same([self.board[r][col] for r in size_range])
        successful_player = successful_player or self.three_same([self.board[i][i] for i in size_range])
        successful_player = successful_player or self.three_same([self.board[i][size-1-i] for i in size_range])

        return successful_player

def play_game():
    board = Board()
    while not board.is_finished():
        if board.get_player() == 'X':
            row = input("Enter row: ")
            col = input("Enter col: ")
            board.make_move(row, col)
        else:
            row, col = board.get_best_move()
            print 'want to go', row, col
            board.make_move(row, col)
        print board

    print "Game Over!"

if __name__ == '__main__':
    board = Board()
    X = 'X'
    O = 'O'
    _ = ' '

    board.set_board([[X,_,X],
                     [O,_,O],
                     [X,O,_]])
    assert board.get_value() == 1

    board.set_board([[X,_,X],
                     [O,_,O],
                     [X,_,_]])
    assert board.get_value() == -1

    board.set_board([[X,_,X],
                     [O,O,O],
                     [X,O,O]])
    assert board.get_value() == -1

    board.set_board([[X,_,_],
                     [_,_,_],
                     [_,_,_]])
    assert board.get_best_move() == (1,1), 'got %r instead' % (board.get_best_move(),)

    play_game()
