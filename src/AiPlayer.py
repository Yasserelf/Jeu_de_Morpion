from Player import Player
from random import randint
import time


class AiPlayer(Player):

    def __init__(self, symbol, color, difficulty):
        super().__init__(symbol, color)
        self.difficulty = difficulty
        self.coup = 0
        self.can_win_O = [[[[0, 0, "O"], [1, 0, "O"], [2, 0, None]], [2, 0]], [[[0, 0, "O"], [1, 0, None], [2, 0, "O"]], [1, 0]], [[[0, 0, None], [1, 0, "O"], [2, 0, "O"]], [0, 0]], [[[0, 1, "O"], [1, 1, "O"], [2, 1, None]], [2, 1]], [[[0, 1, "O"], [1, 1, None], [2, 1, "O"]], [1, 1]], [[[0, 1, None], [1, 1, "O"], [2, 1, "O"]], [0, 1]], [[[0, 2, "O"], [1, 2, "O"], [2, 2, None]], [2, 2]], [[[0, 2, "O"], [1, 2, None], [2, 2, "O"]], [1, 2]], [[[0, 2, None], [1, 2, "O"], [2, 2, "O"]], [0, 2]], [[[0, 0, "O"], [0, 1, "O"], [0, 2, None]], [0, 2]], [[[0, 0, "O"], [0, 1, None], [0, 2, "O"]], [0, 1]], [[[0, 0, None], [0, 1, "O"], [0, 2, "O"]], [
            0, 0]], [[[1, 0, "O"], [1, 1, "O"], [1, 2, None]], [1, 2]], [[[1, 0, "O"], [1, 1, None], [1, 2, "O"]], [1, 1]], [[[1, 0, None], [1, 1, "O"], [1, 2, "O"]], [1, 0]], [[[2, 0, "O"], [2, 1, "O"], [2, 2, None]], [2, 2]], [[[2, 0, "O"], [2, 1, None], [2, 2, "O"]], [2, 1]], [[[2, 0, None], [2, 1, "O"], [2, 2, "O"]], [2, 0]], [[[0, 0, "O"], [1, 1, "O"], [2, 2, None]], [2, 2]], [[[0, 0, "O"], [1, 1, None], [2, 2, "O"]], [1, 1]], [[[0, 0, None], [1, 1, "O"], [2, 2, "O"]], [0, 0]], [[[2, 0, "O"], [1, 1, "O"], [0, 2, None]], [0, 2]], [[[2, 0, "O"], [1, 1, None], [0, 2, "O"]], [1, 1]], [[[2, 0, None], [1, 1, "O"], [0, 2, "O"]], [2, 0]]]
        self.can_win_X = [[[[0, 0, "X"], [1, 0, "X"], [2, 0, None]], [2, 0]], [[[0, 0, "X"], [1, 0, None], [2, 0, "X"]], [1, 0]], [[[0, 0, None], [1, 0, "X"], [2, 0, "X"]], [0, 0]], [[[0, 1, "X"], [1, 1, "X"], [2, 1, None]], [2, 1]], [[[0, 1, "X"], [1, 1, None], [2, 1, "X"]], [1, 1]], [[[0, 1, None], [1, 1, "X"], [2, 1, "X"]], [0, 1]], [[[0, 2, "X"], [1, 2, "X"], [2, 2, None]], [2, 2]], [[[0, 2, "X"], [1, 2, None], [2, 2, "X"]], [1, 2]], [[[0, 2, None], [1, 2, "X"], [2, 2, "X"]], [0, 2]], [[[0, 0, "X"], [0, 1, "X"], [0, 2, None]], [0, 2]], [[[0, 0, "X"], [0, 1, None], [0, 2, "X"]], [0, 1]], [[[0, 0, None], [0, 1, "X"], [0, 2, "X"]], [
            0, 0]], [[[1, 0, "X"], [1, 1, "X"], [1, 2, None]], [1, 2]], [[[1, 0, "X"], [1, 1, None], [1, 2, "X"]], [1, 1]], [[[1, 0, None], [1, 1, "X"], [1, 2, "X"]], [1, 0]], [[[2, 0, "X"], [2, 1, "X"], [2, 2, None]], [2, 2]], [[[2, 0, "X"], [2, 1, None], [2, 2, "X"]], [2, 1]], [[[2, 0, None], [2, 1, "X"], [2, 2, "X"]], [2, 0]], [[[0, 0, "X"], [1, 1, "X"], [2, 2, None]], [2, 2]], [[[0, 0, "X"], [1, 1, None], [2, 2, "X"]], [1, 1]], [[[0, 0, None], [1, 1, "X"], [2, 2, "X"]], [0, 0]], [[[2, 0, "X"], [1, 1, "X"], [0, 2, None]], [0, 2]], [[[2, 0, "X"], [1, 1, None], [0, 2, "X"]], [1, 1]], [[[2, 0, None], [1, 1, "X"], [0, 2, "X"]], [2, 0]]]

    def get_symbol(self):
        return super().get_symbol()

    def get_couleur(self):
        return super().get_couleur()

    def get_diff(self):
        return self.difficulty

    def set_diff(self, diff):
        self.difficulty = diff

    def set_couleur(self, couleur):
        super().set_couleur(couleur)

    def set_symbol(self, symbol):
        super().set_symbol(symbol)

    def check_cell(self, cells, x, y, symbol):
        return cells[x, y] == symbol

    def other_symbol(self):
        if self.get_symbol() == "X":
            return "O"
        else:
            return "X"

    def find_move_win(self, cells):
        if self.get_symbol() == "O":
            rules = self.can_win_O
        else:
            rules = self.can_win_X
        move = None
        for rule in rules:
            if self.check_cell(cells, rule[0][0][0], rule[0][0][1], rule[0][0][2]) and self.check_cell(cells, rule[0][1][0], rule[0][1][1], rule[0][1][2]) and self.check_cell(cells, rule[0][2][0], rule[0][2][1], rule[0][2][2]):
                move = rule[1]
                break
        return move

    def find_move_block(self, cells):
        if self.get_symbol() == "O":
            rules = self.can_win_X
        else:
            rules = self.can_win_O
        move = None
        for rule in rules:
            if self.check_cell(cells, rule[0][0][0], rule[0][0][1], rule[0][0][2]) and self.check_cell(cells, rule[0][1][0], rule[0][1][1], rule[0][1][2]) and self.check_cell(cells, rule[0][2][0], rule[0][2][1], rule[0][2][2]):
                move = rule[1]
                break
        return move

    def play(self, cells, possible_moves):
        move1 = self.find_move_win(cells)
        move2 = self.find_move_block(cells)
        coins_du_board = [(0, 0), (2, 0), (2, 2), (0, 2)]
        if self.difficulty == 0:
            return possible_moves[randint(0, len(possible_moves)-1)]
        elif self.difficulty == 1:

            if move1:
                move = move1
            elif move2:
                move = move2
            elif self.coup == 1:
                for i in range(len(coins_du_board)):
                    m = possible_moves[randint(0, len(coins_du_board)-1)]
                    if m not in coins_du_board:
                        move = m
                        break
                self.coup += 1
            else:
                move = possible_moves[randint(0, len(possible_moves)-1)]
        elif self.difficulty == 2:
            if (1, 1) in possible_moves:
                move = (1, 1)
                self.coup += 1
                self.difficulty = 1
            else:
                for i in range(len(coins_du_board)):
                    m = coins_du_board[randint(0, len(coins_du_board)-1)]
                    if m in possible_moves:
                        move = m
                        break
                self.difficulty = 1
                self.coup += 1

        return move
