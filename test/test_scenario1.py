import pytest
import sys

sys.path.append("../src/")
sys.path.append("../src/interface/")
from MorpionGame import MorpionGame
from GameBoard import GameBoard
from Player import Player

class TestScenario1:

    @pytest.fixture
    def gameboard(self):
        player1 = Player('X', 'red')
        player2 = Player('O', 'blue')
        morpion = MorpionGame(player1, player2)
        gameboard = GameBoard(morpion, 'normal')
        return gameboard

    def test_start_game(self, gameboard):
        gameboard.start() # commencer le jeu
        assert gameboard.is_finished() == False  
        size = gameboard.get_game().get_sizeOfBoard()
        assert len(gameboard.get_game().possibleMovements(gameboard.get_cells())) == size * size

    def test_players(self, gameboard):
        player1 = gameboard.get_game().get_player1()
        player2 = gameboard.get_game().get_player2()
        assert player1.get_couleur() == 'red'
        assert player1.get_symbol() == 'X'
        assert player2.get_couleur() == 'blue'
        assert player2.get_symbol() == 'O'

    def test_move_one_player(self, gameboard):
        gameboard.start()
        size = gameboard.get_game().get_sizeOfBoard()
        assert gameboard.get_coup() == 'X'
        gameboard.play(0,0)
        assert len(gameboard.get_game().possibleMovements(gameboard.get_cells())) == (size * size) - 1
        assert (0,0) not in gameboard.get_game().possibleMovements(gameboard.get_cells())
        assert gameboard.get_coup() == 'O'

    def test_of_winner(self, gameboard):
        size = gameboard.get_game().get_sizeOfBoard()
        cells = gameboard.get_cells()
        assert gameboard.get_coup() == 'X'
        gameboard.play(0,0)
        assert gameboard.get_coup() == 'O'
        assert gameboard.get_game().has_Win(cells) == False
        assert gameboard.get_game().tied_game(cells) == False
        gameboard.play(0,1)
        assert gameboard.get_coup() == 'X'
        gameboard.play(1,0)
        assert gameboard.get_coup() == 'O'
        gameboard.play(1,1)
        assert gameboard.get_game().tied_game(cells) == False
        gameboard.play(2,0)
        assert ((0,0),(0,1),(1,0), (1,1), (2,0))  not in gameboard.get_game().possibleMovements(gameboard.get_cells())
        assert gameboard.get_game().tied_game(cells) == False
        assert gameboard.get_game().has_Win(cells) == True
        assert gameboard.get_game().allign_vertical(cells) == True # c'est la diagonale verticale qui fait gagner 
        assert gameboard.get_game().allign_horizental(cells) == False
        assert gameboard.get_game().allign_diagonal(cells) == False

    def test_of_tied_game(self, gameboard):
        size = gameboard.get_game().get_sizeOfBoard()
        gameboard.play(0,0)
        assert gameboard.get_game().has_Win(gameboard.get_cells()) == False
        assert gameboard.get_game().tied_game(gameboard.get_cells()) == False
        gameboard.play(0,1)
        gameboard.play(0,2)
        gameboard.play(1,0)
        gameboard.play(1,1)
        assert len(gameboard.get_game().possibleMovements(gameboard.get_cells())) == (size * size) - 5
        gameboard.play(2,2)
        gameboard.play(2,1)
        gameboard.play(2,0)
        gameboard.play(1,2)
        assert len(gameboard.get_game().possibleMovements(gameboard.get_cells())) == (size * size) - 9
        assert gameboard.get_game().tied_game(gameboard.get_cells()) == True
        assert gameboard.get_game().has_Win(gameboard.get_cells()) == False

    def test_end_game(self, gameboard):
        gameboard.end() # fin
        assert gameboard.is_finished() == True 
        

if __name__ == '__main__':
    pytest.main()
 