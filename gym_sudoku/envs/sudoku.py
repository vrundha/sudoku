import random
import copy
from typing import Any, Union
import numpy as np

class Sudoku:
    def __init__(self):
        self.puzzle = np.zeros((9, 9), dtype=int)

    def generate(self, n=10):
        """
        Generates a sudoku puzzle
        :param n: number of cells in the puzzle that has to be filled
        """
        for _ in range(n):
            i, j = self.__get_unfilled_cell()
            self.puzzle[i][j] = self.__fill_cell_with_random(i, j)

    def __get_unfilled_cell(self):
        i, j = random.randint(0, 8), random.randint(0, 8)
        return (i, j) if self.puzzle[i][j] == 0 else self.__get_unfilled_cell()

    def check_if_number_ok(self, i, j, number):
        """
        Checks if the number can be added at the index
        :param i: row index
        :param j: column index
        :param number: number to be added
        :return: boolean
        """
        number_ok = True

        for ind in range(9):
            if (ind != j and self.puzzle[i][ind] == number) or (ind !=i and self.puzzle[ind][j] == number):
                number_ok = False

        if number_ok:
            start_i = 3 * (i // 3)
            start_j = 3 * (j // 3)
            for ind_i in range(start_i, start_i + 3):
                for ind_j in range(start_j, start_j + 3):
                    if (not (ind_i == i and ind_j == j)) and self.puzzle[ind_i][ind_j] == number:
                        number_ok = False

        return number_ok

    def __fill_cell_with_random(self, i, j):
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for number in numbers:
            if self.check_if_number_ok(i, j, number):
                return number
        raise RuntimeError("Couldn't fill. Generated an incorrect sudoku puzzle")

    def visualize(self):
        """
        Prints the puzzle in a readable format
        """
        print(self.puzzle)


