"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 8
Topic: 2
Assignment: Unit Test
Date: 02/28/2023
"""

import random
import unittest
from module8_topic2 import average_scores
# from directory.filename import function NOTE: yours might be named something else


class MyTestCase(unittest.TestCase):

    def test_average(self):
        # Arrange
        self.scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54} 
        expected = 39.66666666  # 7 decimal places, remove one and see the test fail
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    def test_average_five(self):
        # Arrange
        self.scores_dict = {}
        for i in range(0,5):
            self.scores_dict.update({f"Test {i}": random.randrange(0, 101)})
        expected = sum(self.scores_dict.values())/len(self.scores_dict)
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    def test_average_zero(self):
        # Arrange
        self.scores_dict = {}

        # Act and Assert
        with self.assertRaises(ValueError):
            average_scores(self.scores_dict)

if __name__ == '__main__':
    unittest.main()