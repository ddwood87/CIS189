"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 13
Topic: 1
Assignment: GUI
Date: 04/11/2023
"""
from NumberGuesserGame import NumberGuesserGame
import tkinter as tk
from tkinter import ttk
import math

class NumberGuesserWindow(tk.Tk):
    game: NumberGuesserGame
    number_count_select_widgets: dict[str, tk.Widget]
    guess_button_widgets: dict[int, tk.Button]
    game_status_bar: tk.Label
    game_frames: dict[int, tk.Frame]
    game_number: int

    def __init__(self):
        super().__init__()
        self.title('Number Guesser Game')
        self.minsize(height = 120, width = 300)
        x_pos = self.winfo_screenwidth()//2 - self.wm_minsize()[0] // 2
        y_pos = self.winfo_screenheight()//2 - self.wm_minsize()[1] // 2
        self.geometry(f'+{x_pos}+{y_pos}')
        self.game_number = 0
        self.create_number_count_widgets()
        self.game_frames = dict()
        self.game_status_bar = tk.Label(self, text='Welcome to Number Guesser Game!')
        self.game_status_bar.pack()
        self.mainloop()

    def reset_game(self):
        number_count = self.number_count_select_widgets['select_slider'].get()
        widgets = self.number_count_select_widgets
        for w in widgets:
            # Skip label widget in this loop
            if w == 'select_label':
                continue
            widgets[w]['state']='disable'
        self.game = NumberGuesserGame(number_count)
        self.game_number += 1
        self.game_status_bar['text']=f'Guess the right number out of {number_count}.'
        self.create_buttons()

    def select_guess_button(self, guess):
        button = self.guess_button_widgets[guess]
        # call make_guess method and check outcome
        if self.game.make_guess(guess):
            button.configure(bg = 'green', disabledforeground='white')
            message = f'{guess} was the correct number!'
            message += f'\nStart a new game!'
            self.game_status_bar.configure(text=message)
            
            self.game_win()
        else:
            self.game_status_bar.configure(text=f'{guess} was incorrect. Guess again!')
            button.configure(state='disabled', bg='red', disabledforeground='white')
            

    def game_win(self):
        buttons = self.guess_button_widgets
        for b in buttons:
            buttons[b].configure(state='disabled')
        widgets = self.number_count_select_widgets
        for w in widgets:
            widgets[w].configure(state='active')
        popup = tk.Tk()
        y_pos = self.winfo_y() - 120
        x_pos = self.winfo_x() - 75
        popup.geometry(f'500x80+{x_pos}+{y_pos}')
        popup.title('Winner!')
        guesses=len(self.game.guessed_list)
        
        tk.Label(popup, text=f'You have won the game in {guesses} guess{"es" if guesses > 1 else ""}!', font=('Arial', 20)).pack()
        tk.Button(popup, text='Continue', command=popup.destroy).pack()

    def create_buttons(self):
        if self.game_number > 1:
            self.game_frames[self.game_number - 1].pack_forget()
        frame = tk.Frame(self)
        self.guess_button_widgets = dict()
        # find rows and columns
        count = self.game.number_count
        sqrt = math.sqrt(count)
        rows = math.ceil(sqrt)
        columns = count//rows
        if count%rows != 0:
            columns += 1
        i = 1
        for row in range(rows):
            for col in range(columns):
                button = tk.Button(frame, 
                                   text=f'{i}', 
                                   name=str(i), 
                                   height = 1,
                                   width = 3,
                                   command = lambda b=i: self.select_guess_button(b))
                
                button.grid(column = col, row = row)
                self.guess_button_widgets[i] = button
                i += 1
                if i > count:
                    break
        self.game_frames[self.game_number] = frame
        frame.pack()

    def number_count_select(self, number_count):
        pass

    def create_number_count_widgets(self):
        frame = tk.Frame(self)
        widgets = dict()
        widgets['select_label'] = tk.Label(frame, text='Select amount of possible numbers: ')
        widgets['select_slider'] = tk.Scale(frame, 
                                            from_=1, 
                                            to=100,
                                            variable=10,
                                            orient='horizontal',
                                            length=100)
        widgets['select_button'] = tk.Button(frame, text='Start Game', command=self.reset_game)
        for w in widgets:
            widgets[w].pack()
        self.number_count_select_widgets = widgets
        frame.pack()

if __name__ == '__main__':
    NumberGuesserWindow()