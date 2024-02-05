from Player import Player
from MorpionGame import MorpionGame
from GameBoard import GameBoard
from AiPlayer import AiPlayer
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
import functools
import sys
sys.path.append('..')


class Configuration(tk.Tk):

    def __init__(self):
        """_summary_
        Attributes :
         symbolOfPlayerAI (String): player symbol
         colorOfPlayerAI : 
         leverOfAI(Int) : player level
        """
        super().__init__()
        self.geometry('750x570')
        self.resizable(width=0, height=0)
        self.title("Morpion Game")
        self.XO = tk.IntVar()
        self.color = tk.IntVar()
        self.AI = tk.StringVar()
        self.symbolOfPlayerAI = ""
        self.colorOfPlayerAI = ""
        self.colorOfPlayer = ""
        self.symbolOfPlayer = ""
        self.leverOfAI = 0
        self._configurate_()

    def _configurate_(self):
        """_summary_
        this function configure AiPlayer:
        -diffNiveau : level of difficulty for AiPlayer
        -symbol1, symbol2 : Ai symbol
        -two buttons : play /  quit
        """
        can = Canvas(self, width=750, height=570, bg="#11213a")
        can.place(x=0, y=0)

        difficulty = tk.Label(master=can, text="Difficulty :", font=font.Font(
            size=30), height=2, bg="#11213a", fg="#d1b57f")
        diffNiveau = ttk.Combobox(
            master=self, value=["Easy", "Medium", "Hard"], textvariable=self.AI, font=(15))
        diffNiveau.current(0)  # niveau easy par défaut
        diffNiveau.place(x=332, y=106)
        diffNiveau.bind("<<ComboboxSelected>>", self.chooseLevel)

        symbol = tk.Label(master=can, text="Symbol  :", font=font.Font(
            size=30), height=2, bg="#11213a", fg="#d1b57f")
        symbol1 = tk.Radiobutton(master=self, text="O", font=font.Font(
            size=30), variable=self.XO, value=1, bg="#11213a", fg="#d1b57f")
        symbol1.place(x=332, y=192)
        symbol1['command'] = functools.partial(self.choose_symbol, symbol1)
        symbol2 = tk.Radiobutton(master=self, text="X", font=font.Font(
            size=30), variable=self.XO, value=2, bg="#11213a", fg="#d1b57f")
        symbol2.place(x=470, y=192)
        symbol2['command'] = functools.partial(self.choose_symbol, symbol2)

        color = tk.Label(master=can, text="Color     :", font=font.Font(
            size=30), height=2, bg="#11213a", fg="#d1b57f")
        color1 = tk.Radiobutton(master=self, text="this", font=font.Font(
            size=30), variable=self.color, value=1, bg="#11213a", fg="#09b5a5")
        color1.place(x=332, y=290)
        color1['command'] = functools.partial(self.choose_color, color1)
        color2 = tk.Radiobutton(master=self, text="this", font=font.Font(
            size=30), variable=self.color, value=2, bg="#11213a", fg="#dca81c")
        color2.place(x=470, y=290)
        color2['command'] = functools.partial(self.choose_color, color2)

        quitButton = tk.Button(master=self, text="Back", font=font.Font(
            size=17), bg="#11213a", fg="#d1b57f", padx=60, pady=5, command=self.back)
        startButton = tk.Button(master=self, text="Play", font=font.Font(
            size=17), bg="#11213a", fg="#d1b57f", padx=62, pady=5, command=self.playAI)

        difficulty.place(x=110, y=72)
        symbol.place(x=110, y=172)
        color.place(x=110, y=272)
        quitButton.place(x=140, y=413)
        startButton.place(x=417, y=413)

    def back(self):
        """_summary_
        back to home page
        """
        self.destroy()
        from Acceuil import Acceuil
        game = Acceuil()
        game.mainloop()

    # récupérer le niveau de difficulté
    def chooseLevel(self, event):
        """_summary_
        Args : event to get the level of AI
        - this level is stocked in difficulty
        - three levels : (0) basic, (1) medium, (2) hard
        """
        difficulty = self.AI.get()
        if (difficulty == "Easy"):
            self.leverOfAI = 0
        elif difficulty == "Medium":
            self.leverOfAI = 1
        else:
            self.leverOfAI = 2

    # récupérer le symbol et la couleur choisie
    def choose_symbol(self, symbol):
        """_summary_
        Args : 
            symbolOfPlayerAI : AI symbol
        this function defines the AI Player symbol, then deduct the simple player symbol 
        """
        self.symbolOfPlayerAI = symbol.cget("text")
        if self.symbolOfPlayerAI == "X":
            self.symbolOfPlayer = "O"
        else:
            self.symbolOfPlayer = "X"

    def choose_color(self, color):
        """_summary_
        Args : 
            colorOfPlayerAI : AI color
        this function defines the AI Player color, then deduct the simple player color 
        """
        self.colorOfPlayerAI = color.cget("fg")
        if self.colorOfPlayerAI == "#dca81c":
            self.colorOfPlayer = "#09b5a5"
        else:
            self.colorOfPlayer = "#dca81c"

    def playAI(self):
        self.destroy()
        self.playerAI = AiPlayer(
            self.symbolOfPlayerAI, self.colorOfPlayerAI, self.leverOfAI)
        self.player = Player(self.symbolOfPlayer, self.colorOfPlayer)
        game = MorpionGame(self.player, self.playerAI)
        board = GameBoard(game, "AI")
        board.mainloop()
