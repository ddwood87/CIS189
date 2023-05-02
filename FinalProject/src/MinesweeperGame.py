"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: Final Project
Topic: Minesweeper Game
Assignment: Game Board
Date: 04/20/2023
"""
import tkinter as tk
import random
import numpy as np
from MinesweeperGame import *
from GameTile import GameTile
import os

class MineSettings:
    class DIFFICULTIES:
        BEGINNER = 'Beginner'
        INTERMEDIATE = 'Intermediate'
        EXPERT = 'Expert'
        CUSTOM = 'Custom'
        ROWS = 'rows'
        COLS = 'cols'
        MINES = 'mines'
        standard_modes = {BEGINNER: {ROWS: 10, COLS: 10, MINES: 20},
                          INTERMEDIATE: {ROWS: 20, COLS: 20, MINES: 60},
                          EXPERT: {ROWS: 40, COLS: 20, MINES: 99}}
    difficulty: str
    rows: int
    cols: int
    mines: int
    # image file keys == value of tile or string description
    image_files: dict = {-1 : 'mine.png', 0: 'zero.png', 1: 'one.png',
                         2: 'two.png', 3: 'three.png', 4: 'four.png',
                         5: 'five.png', 6: 'six.png', 7: 'seven.png', 
                         8: 'eight.png', 'flag': 'flag.png', 'x': 'x.png'}
    image_dir = '\\img\\'

    def __init__(self, 
                 difficulty = DIFFICULTIES.BEGINNER,
                 rows: None | int = None,
                 cols: None | int = None,
                 mines: None | int = None,):
        self.difficulty = difficulty
        if difficulty == self.DIFFICULTIES.CUSTOM:
            self.rows = rows
            self.cols = cols
            self.mines = mines
        else:
            d = self.DIFFICULTIES.standard_modes[difficulty]
            self.rows = d[self.DIFFICULTIES.ROWS]
            self.cols = d[self.DIFFICULTIES.COLS]
            self.mines = d[self.DIFFICULTIES.MINES]

    def get_image(self, image_key):
        curr_path = os.path.abspath(__file__)
        curr_dir = os.path.dirname(curr_path)
        img_dir = curr_dir + self.image_dir
        if image_key == 0:
            # no image
            pass
        else:
            img_path = img_dir + self.image_files[image_key]
            return tk.PhotoImage(file=img_path)
        
class MineGrid(tk.Frame):
    game_tiles: dict[(int,int), GameTile]
    current_key: tuple[int] # key of current tile press, None if not pressing
    active: bool # mouse is hovering current pressed tile
    settings: MineSettings
    exposed_tile_count: int
    
    def __init__(self, master, **options):
        super().__init__(master)
        self.settings = MineSettings()
        if 'difficulty' in options.keys():
            self.config(difficulty=options['difficulty'])
        self.current_press = None
        self.last_press = None
        self.exposed_tile_count = 0

    def config(self, **options):
        self.settings.difficulty = options['difficulty']
        settings = ('rows', 'cols', 'mines')
        for s in settings:
            if s in options:
                self.settings.rows = options[s]

    def get_surrounding_tiles(self, tile: GameTile):
        surround_matrix = {(-1,-1), (-1,0), (-1,1),
                           ( 0,-1),         ( 0,1),
                           ( 1,-1), ( 1,0), ( 1,1)}
        # Add elements of two tuples and return a tuple for translating tile indexes
        def sum_tuple_elements(tuple1, tuple2):
            sum = list()
            for t in zip(tuple1, tuple2):
                sum.append(np.sum(t))
            return tuple(sum)
        
        result = list()
        # Retrieve each tile surrounding a given tile.
        for s in surround_matrix:
            key = tile.key
            neighbor_key = sum_tuple_elements(key, s)
            valid = False
            # Check for valid row key
            if neighbor_key[0] >= 0 and neighbor_key[0] < self.settings.rows:
                # Check for valid column key
                if neighbor_key[1] >= 0 and neighbor_key[1] < self.settings.cols:
                    valid = True
            if valid:
                t = self.game_tiles[neighbor_key]
                result.append(t)    
        return result
    
    def count_surrounding_mines(self, tile):
        if tile.value == -1:
            return tile.value

        surrounding_tiles = self.get_surrounding_tiles(tile)

        count = 0
        for s in surrounding_tiles:
            if s.value == -1:
                count +=1
        return count 

    def build_grid(self):
        rows = self.settings.rows
        cols = self.settings.cols
        mines = self.settings.mines
        spaces_per_mine = rows * cols // mines
        self.game_tiles = dict[(int,int), GameTile]()
        def rand_spaces() -> int:
            return random.randint(0, spaces_per_mine/2)
        
        for r in range(rows):
            for c in range(cols):
                spaces_til_mine = rand_spaces()
                mine = False
                if spaces_til_mine == 0:
                    mine = True
                tile = GameTile(self, mine)
                tile.key = (r,c)
                tile.grid(row = r, column = c)
                tile.bind_events()
                self.game_tiles[r,c] = tile

        keys = self.game_tiles.keys()
        for k in keys:
            t = self.game_tiles[k]
            t.value = self.count_surrounding_mines(t)
            #t.update()

    def depress_tile(self, tile: GameTile):
        tile.depressed = True
        tile.config(relief=tk.SUNKEN)

    def flag_tile(self, tile: GameTile):
        tile.flag_tile()

    def primary_click(self, tile: GameTile):
        if tile.exposed:
            self.exposed_click(tile)         
        else:
            self.expose(tile)

    def secondary_click(self, tile: GameTile):
        if not tile.exposed:
            self.flag_tile(tile)

    def exposed_click(self, tile: GameTile):
        neighbors: list[GameTile]= self.get_surrounding_tiles(tile)
        flag_count = 0
        for t in neighbors:
            if t.flagged:
                flag_count += 1
        if flag_count == tile.value:
            for t in neighbors:
                if t.value == 0:
                    self.expose_zeros(t)
                if not t.flagged:
                    self.expose(t) 
        self.unpress_surrounding(tile) 

    ''''def expose_zero_neighbors(self, tile: GameTile):
        zero_neighbor_keys = set()
        if tile.value == 0:
            for k in zero_neighbor_keys:
                t = self.game_tiles[k]
                if not t.exposed:
                    self.expose(tile)'''

    def expose_surrounding(self, tile: GameTile)-> set:
        surrounding: list[GameTile] = self.get_surrounding_tiles(tile)
        for t in surrounding:            
            if not t.exposed and not t.flagged:
                self.expose(t)
        
    def expose_zeros(self, tile: GameTile, zero_chain: set = None):
        surrounding: list[GameTile] = self.get_surrounding_tiles(tile)
        if zero_chain is None:
            zero_chain = set()
        zero_chain.add(tile.key)

        count = 0
        for t in surrounding:
            if t.value == 0 and t.key not in zero_chain:
                zero_chain.add(t.key)
                t.expose()
                self.exposed_tile_count += 1
                
                zero_chain = self.expose_zeros(t, zero_chain)
            elif t.value > 0:
                count += 1
        if count > 0:
            self.expose_surrounding(tile)
        return zero_chain
    
    def safe_tile_count(self):
        tile_count = self.settings.rows * self.settings.cols
        return tile_count - self.settings.mines

    def expose(self, tile: GameTile):
        self.exposed_til
        if tile.value == 0:
            tile.expose()
            self.expose_zeros(tile)
        elif tile.value == -1:
            self.mine_exposed(tile)
            tile.expose()
        else:
            tile.expose()
        
        self.exposed_tile_count += 1
        safe_tile
        if self.exposed_tile_count == 

    def press_surrounding(self, tile: GameTile):
        surrounding: list[GameTile] = self.get_surrounding_tiles(tile)
        for t in surrounding:
            if not t.flagged:
                t.press()

    def unpress_surrounding(self, tile: GameTile):
        surrounding: list[GameTile] = self.get_surrounding_tiles(tile)
        for t in surrounding:
            t.unpress()
    
    def press_tile(self, tile: GameTile):
        tile.depressed = True

    def unpress_tile(self, tile: GameTile):
        tile.depressed = False
    
    def mine_exposed(self, tile: GameTile):
        tile.selected_mine()
        for k in self.game_tiles:
            t = self.game_tiles[k]
            t.unbind() # disable game tiles
            if t.value == -1:
                # show all unflagged mines
                if not t.flagged:
                    t.expose()
            #x all incorrect flags
            if t.flagged and t.value != -1:
                t.incorrect()

        

    
        
            


import unittest as ut
class test_MineGrid(ut.TestCase):
    def setUp(self) -> None:
        super().setUp()
        difficulty = MineSettings.DIFFICULTIES.BEGINNER
        master = tk.Tk()
        self.grid = MineGrid(master, difficulty=difficulty)

    def test_build_grid(self):
        self.grid.build_grid()
        self.assertTrue(isinstance(self.grid.game_tiles, dict))

    def test_get_surrounding_tiles(self):
        self.grid.build_grid()
        tile = self.grid.game_tiles[(2,2)]
        tiles = self.grid.get_surrounding_tiles(tile)
        self.assertTrue(isinstance(tiles, list))
        self.assertTrue(len(tiles) == 8)

    def test_count_surrounding_mines(self):
        self.grid.build_grid()
        tile = self.grid.game_tiles[(0,0)]
        tile.value = 0
        # set surrounding tile values
        self.grid.game_tiles[(0,1)].value = -1
        self.grid.game_tiles[(1,0)].value = -1
        self.grid.game_tiles[(1,1)].value = 0
        count = self.grid.count_surrounding_mines(tile)
        self.assertEqual(count, 2)
    
if __name__=='__main__':
    #ut.main()
    pass