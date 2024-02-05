from Player import Player
from AiPlayer import AiPlayer
import doctest


class MorpionGame:

    SIZE = 3

    def __init__(self, player1, player2, sizeOfBoard=SIZE):
        self._player1 = player1
        self._player2 = player2
        self._sizeOfBoard = sizeOfBoard

    def get_player1(self):
        return self._player1

    def get_player2(self):
        return self._player2

    def get_sizeOfBoard(self):
        """_summary_

        Returns:
            Integer: the size of board 

        Test:
        >>> game = MorpionGame()
        >>> game.get_sizeOfBoard()
        3
        >>> defaultPlayer1 = Player("X", "blue")
        >>> defaultPlayer2 = Player("O", "red")
        >>> game2 = MorpionGame(defaultPlayer1,defaultPlayer2, 6)
        >>> game2.get_sizeOfBoard()
        6
        """
        return self._sizeOfBoard

    def possibleMovements(self, cells):
        """_summary_

        Args:
            cells (dict): cells of game

        Returns:
            List: list of possible movements, the movement is possible is when the current cell is empty

        Test:
        >>> game = MorpionGame()
        >>> game.possibleMovements({(0,0):"X", (0,1):"X", (0,2):"X", (1,0):"X", (1,1):"O", (1,2):"X", (2,0):None, (2,1):None, (2,2):None})
        [(2, 0), (2, 1), (2, 2)]
        >>> game.possibleMovements({(0,0):None, (0,1):"O", (0,2):"X", (1,0):"O", (1,1):None, (1,2):"O", (2,0):"O", (2,1):"X", (2,2):None})
        [(0, 0), (1, 1), (2, 2)]
        """
        possibleMoves = []
        for i in range(self._sizeOfBoard):
            for j in range(self._sizeOfBoard):
                if not cells[(i, j)]:
                    possibleMoves.append((i, j))
        return possibleMoves

    def allign_horizental(self, cells):
        """_summary_

        Args:
            cells (dict): cells of game

        Returns:
            Bool: True if there is an allign horizontal which allows to win a game

        Test:
        >>> game = MorpionGame()
        >>> game.allign_horizental({(0,0):"X", (0,1):"X", (0,2):"X", (1,0):"X", (1,1):"O", (1,2):"X", (2,0):"O", (2,1):"X", (2,2):"O"})
        True
        >>> game.allign_horizental({(0,0):"X", (0,1):"O", (0,2):"X", (1,0):"O", (1,1):"X", (1,2):"O", (2,0):"O", (2,1):"X", (2,2):"O"})
        False
        """
        aligned = False
        for i in range(self._sizeOfBoard):
            if (cells.get((i, 0)) and cells.get((i, 1)) and cells.get((i, 2)) and (cells[i, 0] == cells[i, 1] == cells[i, 2])):
                aligned = True
        return aligned

    def allign_vertical(self, cells):
        """_summary_

        Args:
            cells (dict): cells of game

        Returns:
            Bool: True if there is an allign vertical which allows to win a game

        Test:
        >>> game = MorpionGame()
        >>> game.allign_vertical({(0,0):"X", (0,1):"O", (0,2):"X", (1,0):"X", (1,1):"O", (1,2):"O", (2,0):"X", (2,1):"X", (2,2):"O"})
        True
        >>> game.allign_vertical({(0,0):"X", (0,1):"X", (0,2):"X", (1,0):"X", (1,1):"O", (1,2):"X", (2,0):"O", (2,1):"X", (2,2):"O"})
        False
        """
        aligned = False
        for i in range(self._sizeOfBoard):
            if (cells.get((0, i)) and cells.get((1, i)) and cells.get((2, i)) and (cells[0, i] == cells[1, i] == cells[2, i])):
                aligned = True
        return aligned

    def allign_diagonal(self, cells):
        """_summary_

        Args:
            cells (dict): cells of game

        Returns:
            Bool: True if there is an allign diagonal which allows to win a game

        Test:
        >>> game = MorpionGame()
        >>> game.allign_diagonal({(0,0):"X", (0,1):"O", (0,2):"O", (1,0):"O", (1,1):"X", (1,2):"O", (2,0):"O", (2,1):"O", (2,2):"X"})
        True
        >>> game.allign_diagonal({(0,0):"X", (0,1):"X", (0,2):"X", (1,0):"X", (1,1):"O", (1,2):"X", (2,0):"O", (2,1):"X", (2,2):"O"})
        False
        """
        aligned = False
        if (cells[0, 0] and cells[1, 1] and cells[2, 2] and (cells[0, 0] == cells[1, 1] == cells[2, 2])):
            aligned = True
        if (cells[0, 2] and cells[1, 1] and cells[2, 0] and (cells[0, 2] == cells[1, 1] == cells[2, 0])):
            aligned = True
        return aligned

    def has_Win(self, cells):
        """_summary_

        Args:
            cells (dict): cells of game

        Returns:
            Bool: True if there is a winner

        Test:
        >>> game = MorpionGame()
        >>> game.has_Win({(0,0):"X", (0,1):"O", (0,2):"O", (1,0):"O", (1,1):"X", (1,2):"O", (2,0):"O", (2,1):"O", (2,2):"X"})
        True
        >>> game.has_Win({(0,0):"X", (0,1):"O", (0,2):"X", (1,0):"O", (1,1):"X", (1,2):"O", (2,0):"O", (2,1):"X", (2,2):"O"})
        False
        """
        return self.allign_vertical(cells) or self.allign_horizental(cells) or self.allign_diagonal(cells)

    def tied_game(self, cells):
        """_summary_

        Args:
            cells (dict): cells of game

        Returns:
            Bool: True if there is no a winner (tied game)

        Test:
        >>> game = MorpionGame()
        >>> game.tied_game({(0,0):"X", (0,1):"O", (0,2):"O", (1,0):"O", (1,1):"X", (1,2):"O", (2,0):"O", (2,1):"O", (2,2):"X"})
        False
        >>> game.tied_game({(0,0):"X", (0,1):"O", (0,2):"X", (1,0):"O", (1,1):"X", (1,2):"O", (2,0):"O", (2,1):"X", (2,2):"O"})
        True
        """
        return (len(self.possibleMovements(cells)) == 0 and self.has_Win(cells) == False)


if __name__ == '__main__':
    doctest.testmod()
