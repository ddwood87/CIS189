"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: Final Project
Topic: Minesweeper Game
Assignment: Custom Game Window
Date: 04/20/2023
"""
import tkinter as tk
from MinesweeperGame import MineSettings

class CustomGameWindow(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)
        self.title('Custom Game')
        self.geometry('200x120')
        icon = self.master.get_icon()
        self.iconphoto(True, icon)
        self.attributes('-toolwindow', True)
        self.pack_window()

    def pack_window(self):
        curr_settings: MineSettings = self.master.get_settings()
        rows = tk.Frame(self)
        cols = tk.Frame(self)
        mines = tk.Frame(self)
        buttons = tk.Frame(self)

        self.row_label = tk.Label(rows, text='Rows: ')
        self.col_label = tk.Label(cols, text='Columns: ')
        self.mine_label = tk.Label (mines, text='Mines: ')

        row_var = tk.StringVar(self, value=curr_settings.rows)
        col_var = tk.StringVar(self, value=curr_settings.cols)
        mine_var = tk.StringVar(self, value=curr_settings.mines)
        self.row_entry = tk.Entry(rows, textvariable=row_var, width=5, justify='right')
        self.col_entry = tk.Entry(cols, textvariable=col_var, width=5, justify='right')
        self.mine_entry = tk.Entry(mines, textvariable=mine_var, width=5, justify='right')

        self.error_label = tk.Label(self, text='')
        self.submit_button = tk.Button(buttons, text='Begin', command = self.submit)
        self.cancel_button = tk.Button(buttons, text='Cancel', command = self.exit)

        self.row_label.pack(side=tk.LEFT)
        self.row_entry.pack(side=tk.RIGHT)
        
        self.col_label.pack(side=tk.LEFT)
        self.col_entry.pack(side=tk.RIGHT)

        self.mine_label.pack(side=tk.LEFT)
        self.mine_entry.pack(side=tk.RIGHT)

        self.submit_button.pack(side=tk.LEFT, padx=5)
        self.cancel_button.pack(side=tk.RIGHT, padx=5)

        rows.pack(fill=tk.X, padx=15)
        cols.pack(fill=tk.X, padx=15)
        mines.pack(fill=tk.X, padx=15)
        self.error_label.pack()
        buttons.pack(side=tk.RIGHT)

    def submit(self):

        try:
            new_rows = int(self.row_entry.get())
            new_cols = int(self.col_entry.get())
            new_mines = int(self.mine_entry.get())
            new_settings = MineSettings()
            new_settings.rows = new_rows
            new_settings.cols = new_cols
            new_settings.mines = new_mines
            self.master.new_settings(new_settings)
            self.destroy()

        except ValueError:
            self.error()
    
    def exit(self):
        self.destroy()

    def error(self):
        self.error_label.config(text='You must enter a number for each field.')

if __name__ == '__main__':
    root = tk.Tk()
    window = CustomGameWindow(root)
    root.mainloop()
