import letter_printer
import os as os
import tkinter as tk


class letter_printer_window:
    def __init__(self, text):
        self.height = 7
        self.width = 100
        self.open_display_window(text)
        self.window.mainloop()

    def open_display_window(self, text: str):
        self.window: tk.Tk = tk.Tk()
        self.window.title("Letter Printer")
        self.window.geometry("300x200+100+200")
        self.window.resizable(True, False)
        self.window.attributes("-alpha", 0.9)

        #display is split into frames because widgets can have only 500 children
        display_frame = tk.Frame(self.window)
        display_frame_count = 0
        display_frame.grid(column=display_frame_count, row=0)
        display_frame.widgetName = [display_frame_count, 0]
        display_frame.setvar('_name', f'col{display_frame_count}row{0}')
        pixel_grid = dict()
        self.frame_grid = dict()
        self.frame_grid[display_frame_count] = pixel_grid
        display_frame_count += 1

        for i in range(self.width):
            for j in range(self.height):
                pixel = tk.Frame(display_frame)
                pixel["height"] = 20
                pixel["width"] = 20
                pixel["bg"] = "grey"
                pixel["borderwidth"] = 2
                pixel["relief"] = "ridge"
                pixel.grid(column=i, row=j)
                pixel_grid[i,j] = pixel
                # pixel.pack()
            if i > 0 and i%70 == 0:
                display_frame = tk.Frame(self.window)
                display_frame.grid(column=display_frame_count, row=0)
                pixel_grid = dict()
                self.frame_grid[display_frame_count] = pixel_grid
                display_frame_count += 1
        self.window.update()
        file = letter_printer.file_accessor("dot_matrix_chars.bin")
        for c in text:
            char = file.get_character(c)
            # draw next char
            lines = char.get_dot_lines()
            for k in lines:
                # cycle length of char column
                #for l in range(0, len(k) - 1):
                    # move all lines left
                self.move_columns_left()
                self.draw_next_column(k)

            # repeat

    def move_columns_left(self):
        display_frame_count = self.width/70
        pixel_grid = self.frame_grid[0]
        display_frame_count += 1
        # having trouble switching between display frames
        for i in range(self.width):
            if i > 0 and i%70 == 1:
                last_grid = pixel_grid
                pixel_grid = self.frame_grid[display_frame_count]
                display_frame_count += 1
            for j in range(self.height):
                if i > 1 and i%70 !=0:
                    pixel_grid[i,j]['bg'] = pixel_grid[i+1,j]['bg']
                # if last column of a display grid
                else:
                    next_pixel = self.frame_grid[][i+1,j]
                    pixel_grid[i,j]['bg'] = next_pixel['bg']


            

    def draw_next_column(self, col):
        # get last column
        last_column = self.width
        for j in range(0, len(col)):
            # find last column
            pixel_grid = self.frame_grid[len(self.frame_grid)-1]
            pixel = pixel_grid[self.width - 1, j]
            if col[j] == "1":
                pixel["bg"] = "red"
            else:
                pixel["bg"] = "black"


class build_chars:
    chars = {
        " ": ["0000000", "0000000", "0000000", "0000000", "0000000"],
        "0": ["0111110", "1000101", "1001001", "1010001", "0111110"],
        "1": ["0000000", "0100001", "1111111", "0000001", "0000000"],
        "2": ["0100001", "1000011", "1000101", "1001001", "0110001"],
        "3": ["1000001", "1001001", "1001001", "1001001", "0110110"],
        "4": ["1111000", "0001000", "0001000", "0001000", "1111111"],
        "5": ["1111001", "1001001", "1001001", "1001001", "1000110"],
        "6": ["0111110", "1001001", "1001001", "1001001", "0000110"],
        "7": ["1000000", "1000000", "1000111", "1001000", "1110000"],
        "8": ["0110110", "1001001", "1001001", "1001001", "0110110"],
        "9": ["0110010", "1001001", "1001001", "1001001", "0111110"],
    }

    def __init__(self, file_name):
        self.file = letter_printer.file_accessor(file_name)

    def build_file(self):
        for r in self.chars:
            c = letter_printer.char(r)
            c.set_dot_lines(self.chars[r])
            self.file.add_char(c)
        self.file.save()


if __name__ == "__main__":
    text = "9957876"
    file_name = "dot_matrix_chars.bin"
    build_chars(file_name).build_file()
    window = letter_printer_window(text)
