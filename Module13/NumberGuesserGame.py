"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 13
Topic: 1
Assignment: GUI
Date: 04/11/2023
"""
import random
import tkinter as tk
from tkinter import messagebox
import unittest
class NumberGuesserGame:

    number_count: int
    winning_number: int
    guessed_list: set
    
    def __init__(self, number_count):
        self.number_count = number_count
        self.guessed_list = set()
        self.reset_game(self.number_count)

    #@classmethod
    def reset_game(self, number_count):
        # set new winning number, new guessed list
        if number_count > 100:
            raise ValueError('Must select 100 numbers or less.')
        self.winning_number = random.randint(1, number_count)
        if len(self.guessed_list) > 0:
            del self.guessed_list
            self.guessed_list = set()

    #@classmethod
    def make_guess(self, guess) -> bool:
        # Returns false if incorrect, true if correct
        self.guessed_list.add(guess)
        if guess == self.winning_number:
            #print(f'{guess} is the winning number!')
            return True
        else:
            #print(f'{guess} is not the winning number.')
            return False

class TestNumberGuesser(unittest.TestCase):
    def setUp(self):
        self.number_count = 10
        self.winning_number = 3
        self.game = NumberGuesserGame(self.number_count)
        self.game.winning_number = self.winning_number

    def tearDown(self) -> None:
        del self.number_count
        del self.winning_number
        del self.game
        return super().tearDown()
    
    def test_reset_game(self):
        guesses = reversed(range(3))
        count = 0
        for i in guesses:
            self.game.make_guess(self.winning_number+i)
            count += 1
        self.assertEqual(len(self.game.guessed_list), count)
        self.game.reset_game(self.number_count)
        self.assertEqual(len(self.game.guessed_list), 0)

    def test_make_guess_incorrect(self):
        self.assertEqual(len(self.game.guessed_list), 0)
        self.assertFalse(self.game.make_guess(self.winning_number+1))
        self.assertEqual(len(self.game.guessed_list), 1)

    def test_make_guess_correct(self):
        self.assertEqual(len(self.game.guessed_list), 0)
        self.assertTrue(self.game.make_guess(self.winning_number))
        self.assertEqual(len(self.game.guessed_list), 1)

if __name__ == '__main__':
    unittest.main()