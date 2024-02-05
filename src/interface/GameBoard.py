from MorpionGame import MorpionGame
import tkinter as tk
from tkinter import font
import doctest
import time
import sys
sys.path.append("..")


# Tk() : permet de créer la fenètre de base pour le jeu
class GameBoard(tk.Tk):

    def __init__(self, game, mode):
        """_summary_    
        Args: 
            game : the morpion game
            mode : "normal" or "AI"

        Attributes : 
        cells : dict{key:coordonnée de la cellule,  value:"X" ou "O"}
        buttons : dict{key:coordonnée de la cellule,  value:button}
        game(MorpionGame) : : morpion game
        grill : la grille du jeu
        coup(String): par défaut "X"
        finish(Bool): initialement faux
        """
        super().__init__()
        self.title("Morpion Game")
        self.geometry('750x570')
        self.resizable(width=0, height=0)
        self.config(bg="#11213a")
        self._cells = {}
        self.game = game
        self.buttons = {}
        self.grille = tk.Frame(bg="#11213a")
        self.createBoard()
        self.createGameBoard()
        self._optionsButton_()
        self.coup = "X"
        self.mode = mode  # "normal" or "AI"
        # self.finish = False
        self.start()

    def is_finished(self):
        return self.finish

    def start(self):
        self.finish = False

    def end(self):
        self.finish = True
        for i in self.buttons:
            self.buttons[i[0], i[1]].configure(state="disabled")

    def get_cells(self):
        """_summary_    
        Returns : the dict of cells => keys=(position,position), value=symbol
        """
        return self._cells

    def get_buttons(self):
        """_summary_    
        Returns : the dict of buttons => keys=(position,position), value=button
        """
        return self.buttons

    def get_grille(self):
        """_summary_    
        Returns : the the grill of game
        """
        return self.grille

    def get_game(self):
        """_summary_    
        Returns : the game
        """
        return self.game

    def get_coup(self):
        """_summary_    
        Returns : the choice : 'X' or 'O'
        """
        return self.coup

    def createBoard(self):
        """_summary_    
        le paneau d'affichage
        """
        cadre = tk.Frame()  # création du cadre de l'interface
        cadre.pack()
        self.entete = tk.Label(cadre, text="", font=font.Font(
            size=30, weight="bold"), bg="#11213a")  # création d'un entete dans le cadre
        self.entete.pack()

    def createGameBoard(self):
        """_summary_    
        create the board of the game  (création de la grille de cellules)
        """
        self.start()
        self.entete["text"] = 'New Game'
        self.entete["fg"] = "White"
        # création du cadre des cellules
        self.grille.pack()
        for i in range(3):
            for j in range(3):
                # créer un bouton pour chaque cellule
                button = tk.Button(self.grille, text="", font=font.Font(size=22, weight="bold"), bg="#ead5ba",
                                   fg="black", width=10, height=3, command=lambda row=i, col=j: self.play(row, col))
                button.configure(state="normal")  # bouton cliquable
                # chaque bouton est une clé, sa valeur c'est ses dimensions (dictionnaire)
                self._cells[(i, j)] = None
                self.buttons[i, j] = button
                # grid pour organiser et espacer le bouton
                button.grid(row=i, column=j, padx=5, pady=5)

    def _back_(self):
        """_summary_    
        destroy the current page, and back to the home page
        """
        self.destroy()
        from Acceuil import Acceuil
        game = Acceuil()
        game.mainloop()

    def replay(self):
        """_summary_    
        call createGameBoard() to replay
        """
        self.start()
        self.createGameBoard()

    def _optionsButton_(self):
        """_summary_    
        this function presents two options : 
        back and restart
        """
        backButton = tk.Button(master=self, text="Back", font=font.Font(
            size=17), bg="#11213a", fg="#d1b57f", padx=60, pady=5, command=self._back_)
        restartButton = tk.Button(master=self, text="Replay", font=font.Font(
            size=17), bg="#11213a", fg="#d1b57f", padx=62, pady=5, command=self.createGameBoard)

        backButton.place(x=137, y=500)
        restartButton.place(x=415, y=500)

    def X_Played(self, row, col):
        """_summary_
        Args: 
            row(int) : the horizental position of the choice
            col(int) : the vertical position of the choice

        updates : the current cell (row, col) takes "X" 
        """
        self._update_turn("X", "#09b5a5")
        self.buttons[row, col].config(text="X", fg="#09b5a5")
        self._cells[row, col] = "X"
        self.coup = "O"

    def O_Played(self, row, col):
        """_summary_
        Args: 
            row(int) : the horizental position of the choice
            col(int) : the vertical position of the choice

        updates : the current cell (row, col) takes "O" 
        """
        self._update_turn("O", "#dca81c")
        self.buttons[row, col].config(text="O", fg="#dca81c")
        self._cells[row, col] = "O"
        self.coup = "X"

    def _update_turn(self, text, fg):
        """_summary_    
        Args: 
            msg : the symbol of player : "X" or "O"
            fg : text color

        display the player's turn
        """
        self.entete["text"] = f"{text}'s turn"
        self.entete["fg"] = fg

    def _update_tied(self):
        self.entete["text"] = 'Tied Game !'
        self.entete["fg"] = "red"

    def _update_winner(self, msg, color="black"):
        """_summary_    
        Args: 
            msg : the symbol of player : "X" or "O"
            color : display color

        display the game's winner
        """
        self.entete["text"] = f'Player "{msg}" won!'
        self.entete["fg"] = color

    def playAgainstAI(self, row, col, symbol, color):
        """_summary_    
        Args: 
            row : line position
            col : column position
            symbol : player symbol 
            color : player color
        the simple player use playAgainstAI to play against playerAI
        """
        self._update_turn(symbol, color)
        self.buttons[row, col].config(text=symbol, fg=color)
        self._cells[row, col] = symbol

    def playAgainstUser(self, symbolAI, colorAI, move):
        """_summary_    
        Args: 
            symbolAI : playerAI symbol 
            colorAI : playerAI color
            move : the move returned by play of AI (some cell)
        it's the turn of AI
        """
        self.buttons[move[0], move[1]].config(text=symbolAI, fg=colorAI)
        self._cells[move[0], move[1]] = symbolAI
        # self._update_turn(symbolAI, colorAI)

    def play(self, row, col):
        """_summary_
        Args: 
            row(int) : the horizental position of the choice
            col(int) : the vertical position of the choice
        Returns:
            Bool: True if the player can play, False else (when there is winner or tied game) 

        Test:
        >>> game = MorpionGame()
        >>> gameboard = GameBoard(game, "normal")
        >>> gameboard.play(1,1)
        True
        >>> gameboard._cells={(0,0):None, (0,1):None, (0,2):None, (1,0):None, (1,1):None, (1,2):None, (2,0):None, (2,1):None, (2,2):"X"}
        >>> gameboard.play(2,2)
        False
        >>> gameboard.play(0,0)
        True
        """
        ret = False
        self.start()
        if not self.is_finished():
            if self.mode == "normal":
                if (row, col) in self.game.possibleMovements(self._cells):
                    ret = True
                    if self.coup == "X":
                        self.X_Played(row, col)
                        if self.game.has_Win(self._cells):
                            self._update_winner(msg="X", color="#09b5a5")
                            self.end()
                    elif self.coup == "O":
                        self.O_Played(row, col)
                        if self.game.has_Win(self._cells):
                            self._update_winner(msg="O", color="#dca81c")
                            self.end()
                    if self.game.tied_game(self._cells):
                        self._update_tied()

            elif self.mode in {"AI", "Ai", "ai"}:
                if (row, col) in self.game.possibleMovements(self._cells):
                    symbol = self.game.get_player1().get_symbol()
                    color = self.game.get_player1().get_couleur()
                    self.playAgainstAI(row, col, symbol, color)
                    if self.game.has_Win(self._cells):
                        self._update_winner(msg=symbol, color=color)
                        self.end()

                    elif self.game.tied_game(self._cells):
                        self._update_tied()
                        self.end()
                    else:
                        symbolAI = self.game.get_player2().get_symbol()
                        colorAI = self.game.get_player2().get_couleur()
                        move = self.game.get_player2().play(
                            self._cells, self.game.possibleMovements(self._cells))
                        self.playAgainstUser(symbolAI, colorAI, move)
                        if self.game.has_Win(self._cells):
                            self._update_winner(msg=symbolAI, color=colorAI)
                            self.end()
                        elif self.game.tied_game(self._cells):
                            self._update_tied()
                            self.end()
        else:
            self.buttons[row, col].config(text="")


if __name__ == '__main__':
    doctest.testmod()
