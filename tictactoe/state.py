import numpy as np

from .player import Player


class State():
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.winner = None
        self.end = None
        self.current_state = []
        self.current_player = None
        self.previous_player = None
        self.next_state = None
        return

    def move_ok(self, r, c):
        if self.current_state.board[r, c] != 0:
            return True
        else:
            return False

    def render(self):
        # clear_output()
        temp_board = self.board.tolist()
        for i in range(len(temp_board)):
            for j in range(len(temp_board)):
                if temp_board[i][j] == 1:
                    temp_board[i][j] = "O"
                if temp_board[i][j] == -1:
                    temp_board[i][j] = "X"
                elif temp_board[i][j] == 0.0:
                    temp_board[i][j] = "*"

        print(f' {temp_board[0][0]}|{temp_board[0][1]}|{temp_board[0][2]}\n-------\n {temp_board[1][0]}|{temp_board[1][1]}|{temp_board[1][2]}\n-------\n {temp_board[2][0]}|{temp_board[2][1]}|{temp_board[2][2]}')

    def checker(self):
        if self.end is not None:
            return self.end
        result = []
        for i in range(len(self.board)):
            result.append(np.sum(self.board[i, :]))

        for i in range(len(self.board)):
            result.append(np.sum(self.board[:, i]))

        cross = 0
        for i in range(len(self.board)):
            cross += self.board[i, i]
        result.append(cross)

        othercross = 0
        j = len(self.board) - 1
        for i in range(len(self.board)):
            othercross += self.board[i, j]
            j -= 1
        result.append(othercross)

        for i in result:
            if i == 3:
                self.winner = 1
                self.end = True
                return self.end
            if i == -3:
                self.winner = -1
                self.end = True
                return self.end

        istie = True
        for i in result:
            if i == 0.0:
                istie = False
            if istie == True:
                self.winner = 0
                self.end = True
                return self.end

    def checker2(self):
        if self.end is not None:
            return self.end
        result = []
        # row check p1

        if self.board[0][0] == self.board[0][1] == self.board[0][2] == 1 or self.board[1][0] == self.board[1][1] == self.board[1][2] == 1 or self.board[2][0] == self.board[2][1] == self.board[2][2] == 1:
            self.end = True
            self.winner = 1
            return self.end

        # colums check p1
        if self.board[0][0] == self.board[1][0] == self.board[2][0] == 1 or self.board[0][1] == self.board[1][1] == self.board[2][1] == 1 or self.board[0][2] == self.board[1][2] == self.board[2][2] == 1:
            self.end = True
            self.winner = 1
            return self.end
        # crosses p1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 1 or self.board[0][2] == self.board[1][1] == self.board[2][0] == 1:
            self.end = True
            self.winner = 1
            return self.end

        # row check p2
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == -1 or self.board[1][0] == self.board[1][1] == self.board[1][2] == -1 or self.board[2][0] == self.board[2][1] == self.board[2][2] == -1:
            self.end = True
            self.winner = -1

            return self.end
        # colums check p2
        if self.board[0][0] == self.board[1][0] == self.board[2][0] == -1 or self.board[0][1] == self.board[1][1] == self.board[2][1] == -1 or self.board[0][2] == self.board[1][2] == self.board[2][2] == -1:
            self.end = True
            self.winner = -1
            return self.end
        # crosses p2
        # crosses p1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == -1 or self.board[0][2] == self.board[1][1] == self.board[2][0] == -1:
            self.end = True
            self.winner = -1
            return self.end

        # Draw check
        if self.board[0][0] != 0 and self.board[0][1] != 0 and self.board[0][2] != 0 and self.board[1][0] != 0 and self.board[1][1] != 0 and self.board[1][2] != 0 and self.board[2][0] != 0 and self.board[2][1] != 0 and self.board[2][2] != 0:
            self.winner = 0
            self.end = True
            return self.end

        return self.end

    def reset(self):
        self.current_state = self.board
        player_one = Player()
        player_two = Player()
        return
