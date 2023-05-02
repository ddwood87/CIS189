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
class SegmentChar(tk.Canvas):
    pass
class SegmentDisplay(tk.Frame):
    segment_chars: list[SegmentChar]

    # 3 sets of segment display
    def __init__(self, master):
        super().__init__(master)



class MineDisplay(SegmentDisplay):
    pass
class TimerDisplay(SegmentDisplay):
    pass
class ResetButton(tk.Button):
    def __init__(self):
        super().__init__()

class MineHeader(tk.Frame):
    mine_count_display: MineDisplay
    timer_display: TimerDisplay
    reset_button: ResetButton

    def __init__(self, master):
        super().__init__(master)

class MainGameFrame(tk.Tk):
    menu_frame: MineMenu
    game_stats_frame: MineHeader
    game_grid_frame: MineGrid

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Minesweeper')
        #self.menu_frame = MineMenu(self)
        #self.game_stats_frame = MineHeader(self)
        self.game_grid_frame = MineGrid(self)
        self.game_grid_frame.build_grid()

        #tiles = self.game_grid_frame.game_tiles
        #for t in tiles:
            #tiles[t].image_label.bind('<ButtonPress>', self.button_press)
            #tiles[t].image_label.bind('<ButtonRelease>', self.button_release)

        #self.menu_frame.pack()
        #self.game_stats_frame.pack()
        self.game_grid_frame.focus_set()
        self.game_grid_frame.pack()

    def button_press(self, event):
        print('Button press')

    def button_release(self, event):
        print('Button release')

if __name__ == '__main__':
    
    game = MainGameFrame()
    game.mainloop()


