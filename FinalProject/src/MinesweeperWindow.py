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
from GameStatusFrame import *
from MineMenuFrame import *
from CustomGameWindow import CustomGameWindow

class MainGameWindow(tk.Tk):
    menu_frame: MineMenu
    game_status_frame: MineStatus
    game_grid_frame: MineGrid

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Minesweeper')
        icon = self.get_icon()
        self.iconphoto(True, icon)
        self.config(bd=5, relief = tk.FLAT)
        self.menu_frame = MineMenu(self)
        self.game_grid_frame = MineGrid(self)
        self.game_status_frame = MineStatus(self)

        self.menu_frame.pack()
        self.game_status_frame.pack(fill=tk.X, pady=6)
        self.game_grid_frame.focus_set()
        self.game_grid_frame.pack()

    def get_icon(self):
        curr_path = os.path.abspath(__file__)
        curr_dir = os.path.dirname(curr_path)
        img_dir = curr_dir + '\\img\\'
        img_path = img_dir + 'mine.png'
        return tk.PhotoImage(file=img_path)
    
    def game_win(self):
        self.game_status_frame.win()

    def game_loss(self):
        self.game_status_frame.loss()

    def reset_game(self):
        self.game_status_frame.reset_status()
        self.game_grid_frame.reset()

    def start(self):
        self.game_status_frame.start()

    def flag(self):
        self.game_status_frame.flag()

    def unflag(self):
        self.game_status_frame.unflag()
    
    def get_settings(self):
        return self.game_grid_frame.settings

    def get_mine_count(self):
        settings = self.get_settings()
        return settings.mines
    
    def beginner(self):
        self.game_grid_frame.config(difficulty=MineSettings.DIFFICULTIES.BEGINNER)
        self.reset_game()

    def intermediate(self):
        self.game_grid_frame.config(difficulty=MineSettings.DIFFICULTIES.INTERMEDIATE)
        self.reset_game()

    def expert(self):
        self.game_grid_frame.config(difficulty=MineSettings.DIFFICULTIES.EXPERT)
        self.reset_game()

    def custom_diff(self):
        customize_window = CustomGameWindow(self)

    def new_settings(self, settings: MineSettings):
        self.game_grid_frame.settings = settings
        self.reset_game()

    def exit(self):
        self.quit()

if __name__ == '__main__':
    
    game = MainGameWindow()
    game.mainloop()


