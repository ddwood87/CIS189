"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: Final Project
Topic: Minesweeper Game
Assignment: Root Window
Date: 04/20/2023
"""
import tkinter as tk
from MinesweeperGame import *

class MineMenu(tk.Frame):
    game_menu: tk.Menu

    def __init__(self, master):
        super().__init__(master)
        self.game_menu = tk.Menu(self)
        master.config(menu=self.game_menu)

        game_menu = tk.Menu(self.game_menu)
        self.game_menu.add_cascade(label="Game", menu=game_menu)

        diff_menu= tk.Menu(game_menu)
        game_menu.add_cascade(label="Difficulty", menu=diff_menu)
        diff_menu.add_command(label='Beginner',command=self.master.beginner)
        diff_menu.add_command(label='Intermediate',command=self.master.intermediate)
        diff_menu.add_command(label='Expert',command=self.master.expert)


        game_menu.add_separator()
        game_menu.add_command(label='Reset', command=self.master.reset_game)

        game_menu.add_separator()
        game_menu.add_command(label='Exit', command=self.master.exit)

if __name__=='__main__':
    root = tk.Tk()
    menu = MineMenu(root)
    menu.pack()
    root.mainloop()