from MorpionGame import MorpionGame
from Configuration import Configuration
from tkinter import *
from tkinter import font
import tkinter as tk
import sys
sys.path.append("..")


class Acceuil(tk.Tk):

    def __init__(self):
        """_summary_
        Attributes :
         img(PhotoImage) : the background of the game
        """
        super().__init__()
        self.geometry('610x570')
        self.resizable(width=0, height=0)
        self.title("Morpion Game")
        self.img = PhotoImage(file="../labels/background.png")
        self._createMenu_()

    def playWithUser(self):
        """_summary_
        destruct the current page, 
        create normal game between two players
        """
        self.destroyPage()
        from GameBoard import GameBoard
        from Player import Player
        player1 = Player("X", "red")
        player2 = Player("O", "blue")
        game = MorpionGame(player1, player2)
        x = GameBoard(game, "normal")
        x.mainloop()

    def playWithAI(self):
        """_summary_
        destruct the current page, 
        create AI game between user and AI
        """
        self.destroyPage()
        x = Configuration()
        x.mainloop()

    def destroyPage(self):
        """_summary_
        destruct the current page, to quit game
        """
        self.destroy()

    def _createMenu_(self):
        """_summary_
        create Menu with a canva
        3 buttons : 
        1- Simple game (between two users)
        2- Configure game with AI
        3- Quit game
        """
        can = Canvas(self, width=620, height=570)
        can.create_image(0, 0, anchor=NW, image=self.img)
        can.place(x=0, y=0)

        entete = tk.Label(master=self, text="Menu Principal", font=font.Font(
            size=40, weight="bold"), height=2, bg="#11213a", fg="#e9d4ba")
        button1 = tk.Button(master=self, text="Partie rapide", font=font.Font(
            size=21), bg="#11213a", fg="#e9d4ba", command=self.playWithUser)
        button2 = tk.Button(master=self, text="Configurer AI", font=font.Font(
            size=17), bg="#11213a", fg="#e9d4ba", command=self.playWithAI)
        button3 = tk.Button(master=self, text="Quitter", font=font.Font(
            size=23), bg="#11213a", fg="#e9d4ba", command=self.destroyPage)

        entete.pack(padx=10, pady=30)
        button1.pack(padx=50, pady=13)
        button2.pack(padx=50, pady=13)
        button3.pack(padx=50, pady=13)
