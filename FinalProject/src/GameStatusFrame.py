"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: Final Project
Topic: Minesweeper Game
Assignment: Game Status Frame
Date: 04/20/2023
"""
import tkinter as tk
import time
from MinesweeperGame import *

class SegmentChar(tk.Canvas):
    off_color = '#333'
    on_color = '#f33'
    segments: dict
    CHARS = {0:(1,0,1,1,1,1,1),
             1:(0,0,0,0,0,1,1),
             2:(1,1,1,0,1,1,0),
             3:(1,1,1,0,0,1,1),
             4:(0,1,0,1,0,1,1),
             5:(1,1,1,1,0,0,1),
             6:(1,1,1,1,1,0,1),
             7:(1,0,0,0,0,1,1),
             8:(1,1,1,1,1,1,1),
             9:(1,1,1,1,0,1,1),
             'E':(1,1,1,1,1,0,0),
             '-':(0,1,0,0,0,0,0)}
    
    def __init__(self, master):
        super().__init__(master, bg='black', height=34, width= 21, bd=-2)
        self.create_segments()

    def update(self, number):
        if 0<=number<=9:
            char = self.CHARS[number]
            for (c, s) in zip(char, self.segments):
                if c == 0:
                    self.itemconfig(self.segments[s], fill=self.off_color)
                elif c == 1:
                    self.itemconfig(self.segments[s], fill=self.on_color)
        if number == -1:
            char = self.CHARS['-']
            for (c, s) in zip(char, self.segments):
                if c == 0:
                    self.itemconfig(self.segments[s], fill=self.off_color)
                elif c == 1:
                    self.itemconfig(self.segments[s], fill=self.on_color)

    def create_segment(self, coords):
        return self.create_polygon(coords, fill=self.off_color)

    def create_segments(self):
        self.segments = dict()
        first_segment = list((4,4, 7,2, 14,2, 17,4, 14,6, 7,6))
        # three horizontal segments
        seg = first_segment
        translate = 13
        for i in range(0,3):
            self.segments[i] = self.create_segment(seg)
            seg = self.translate(seg, 0, translate)
        # two left segments
        seg = self.rotate(first_segment, 90)
        for i in range(3,5):
            self.segments[i] = self.create_segment(seg)
            seg = self.translate(seg, 0, translate)
        # two right segments
        seg = self.translate(seg, translate, -(translate*2))
        for i in range(5,7):
            self.segments[i] = self.create_segment(seg)
            seg = self.translate(seg, 0, translate)
        '''self.segments[2] = self.translate(self.segments[1], 0, 15)
        for i in range(0,3):
            self.segments[i] = self.create_segment(self.segments[i])
            #self.segments[i].pack(side=tk.LEFT)
            pass'''

    def rotate(self, segment, degrees):
        if degrees == 90:
            for i in range(0, 12, 2):
                temp = segment[i]
                segment[i] = segment[i+1]
                segment[i+1] = temp
        return segment

    def translate(self, segment, x, y):
        new_segment = list()
        count = 0
        for n in segment:
            if count%2 == 0:
                new_segment.append(n+x)
            else:
                new_segment.append(n+y)
            count += 1
        return new_segment

class SegmentDisplay(tk.Frame):
    segment_chars: list[SegmentChar]# 3 sets of segment display
    value: int
    
    def __init__(self, master):
        super().__init__(master)
        self.segment_chars = dict[int, SegmentChar]()
        for i in range(0,3):
            self.segment_chars[i] = SegmentChar(self)
            self.segment_chars[i].pack(side=tk.LEFT)

    def update_segments(self, number):
        if number < 1000:
            number_string = str(number)
            length = len(number_string)
            if number >= 0:
                if length == 3:
                    for i in range(0,3):
                        self.segment_chars[i].update(int(number_string[i]))
                if length == 2:
                    self.segment_chars[0].update(0)
                    for i in range(0,2):
                        self.segment_chars[i+1].update(int(number_string[i]))
                if length < 2:
                    self.segment_chars[0].update(0)
                    self.segment_chars[1].update(0)
                    i = 0
                    self.segment_chars[i+2].update(int(number_string[i]))
            elif number > -100:
                number_string = number_string[1:]
                self.segment_chars[0].update('-')
                if length == 3:
                    for i in range(0,2):
                        self.segment_chars[i+1].update(int(number_string[i]))
                else:
                    self.segment_chars[1].update(int(number_string[0]))
                    
        else:
            self.segment_chars[2].update('E')
        
class MineDisplay(SegmentDisplay):
    def __init__(self, master):
        super().__init__(master)

    def update(self, number):
        self.value = number
        self.update_segments(self.value)

class TimerDisplay(SegmentDisplay):
    def __init__(self, master):
        super().__init__(master)
        self.value = 0

    def update(self):
        self.update_segments(self.value)
        if self.master.play:
            timer = time.time() - self.master.start_time 
            self.value = int(timer)
            self.after(1000, self.update)

    def reset(self):
        self.value = 0
        self.update()

class ResetButton(tk.Button):
    IMAGES = {'reset': 'reset.png',
              'winner': 'winner.png',
              'loser': 'loser.png'}
    IMAGE_DIR = '\\img\\'

    def __init__(self, master):
        super().__init__(master, command=self.reset)
        img = self.get_image('reset')
        self.image = img
        self.config(image=img) 

    def get_image(self, image_key):
        curr_path = os.path.abspath(__file__)
        curr_dir = os.path.dirname(curr_path)
        img_dir = curr_dir + self.IMAGE_DIR
        img_path = img_dir + self.IMAGES[image_key]
        return tk.PhotoImage(file=img_path)

    def reset(self):
        self.reset_image()
        self.master.reset_game()

    def reset_image(self):
        img = self.get_image('reset')
        self.image = img
        self.config(image=img)

    def win(self):
        img = self.get_image('winner')
        self.image = img
        self.config(image=img)
    
    def loss(self):
        img = self.get_image('loser')
        self.image = img
        self.config(image=img)

class MineStatus(tk.Frame):
    mine_count_display: MineDisplay
    timer_display: TimerDisplay
    start_time: float
    play_time: int
    play: bool
    reset_button: ResetButton
    mine_count: int
    def __init__(self, master):
        super().__init__(master)
        self.play = False
        self.mine_count = self.master.get_mine_count()
        self.mine_count_display = MineDisplay(self)
        self.mine_count_display.update(self.mine_count)
        self.timer_display = TimerDisplay(self)
        self.timer_display.reset()
        self.reset_button = ResetButton(self)
        self.mine_count_display.pack(side=tk.LEFT)
        self.timer_display.pack(side=tk.RIGHT)
        self.reset_button.pack(side= tk.BOTTOM)
    
    def win(self):
        self.play_time = time.time() - self.start_time 
        self.reset_button.win()
        self.play = False
        
    def loss(self):
        self.play_time = time.time() - self.start_time 
        self.reset_button.loss()
        self.play = False

    def flag(self):
        self.mine_count -= 1
        self.mine_count_display.update(self.mine_count)
    
    def unflag(self):
        self.mine_count += 1
        self.mine_count_display.update(self.mine_count)
    
    def start(self):
        self.start_time = time.time()
        self.play = True
        self.timer_display.update()

    def reset_game(self):
        self.play = False
        self.reset_status()
        self.master.reset_game()

    def reset_status(self):
        self.play = False
        self.reset_button.reset_image()
        self.mine_count = self.master.get_mine_count()
        self.mine_count_display.update(self.mine_count)
        self.timer_display.reset()