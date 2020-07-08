class TicTacToe:

    def print_board(self):
        print(f'''---------
| {self.cells[0]} {self.cells[1]} {self.cells[2]} |
| {self.cells[3]} {self.cells[4]} {self.cells[5]} |
| {self.cells[6]} {self.cells[7]} {self.cells[8]} |
---------''')
        self.status()

    def status(self):
        self.horizontal = [[self.cells[x * 3], self.cells[x * 3 + 1], self.cells[x * 3 + 2]] for x in range(0, 3)]
        self.vertical = [[self.cells[x], self.cells[3 + x], self.cells[6 + x]] for x in range(0, 3)]
        self.diagonal = [[self.cells[0], self.cells[4], self.cells[8]], [self.cells[2], self.cells[4], self.cells[6]]]
        self.combinations = self.horizontal + self.vertical + self.diagonal
        if any([1 for x in range(len(self.combinations)) if self.combinations[x] == ['X', 'X', 'X']]):
            print('X wins')
            quit()
        elif any([1 for x in range(len(self.combinations)) if self.combinations[x] == ['O', 'O', 'O']]):
            print('O wins')
            quit()
        elif not (' ' in self.cells):
            print('Draw')
            quit()
        if self.player == 'X':
            self.player = 'O'
            self.make_move()
        else:
            self.player = 'X'
            self.make_move()

    def make_move(self):
        self.x, self.y = input('Enter the coordinates: ').split()
        if self.x not in '123' or self.y not in '123':
            print("You should enter numbers!")
            self.make_move()
        elif not (1 <= int(self.x) <= 3) or not (1 <= int(self.y) <= 3):
            print("Coordinates should be from 1 to 3!")
            self.make_move()
        self.cells_map = [[[1, 3], 0], [[2, 3], 1], [[3, 3], 2],
                     [[1, 2], 3], [[2, 2], 4], [[3, 2], 5],
                     [[1, 1], 6], [[2, 1], 7], [[3, 1], 8]]
        self.cell_move = [self.cells_map[i][1] for i in
                          range(len(self.cells_map)) if self.cells_map[i][0] == [int(self.x), int(self.y)]]
        if self.cells[self.cell_move[0]] == ' ':
            self.cells[self.cell_move[0]] = self.player
            self.print_board()
        else:
            print("This cell is occupied! Choose another one!")
            self.make_move()

    def play(self):
        self.cells = list('         ')
        self.player = 'O'
        self.print_board()


game = TicTacToe()
game.play()
