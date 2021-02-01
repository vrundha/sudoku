import random
import copy
from typing import Any, Union
import numpy as np

class Sudoku:

    def __init__(self):
        self.puzzle = np.zeros((9, 9), dtype=int)

    def generate(self, n=10):
        for _ in range(n):
            i, j = self.__get_unfilled_cell()
            self.puzzle[i][j] = self.__fill_cell_with_random(i, j)

    def __get_unfilled_cell(self):
        i, j = random.randint(0, 8), random.randint(0, 8)
        return (i, j) if self.puzzle[i][j] == 0 else self.__get_unfilled_cell()

    def check_if_number_ok(self, i, j, number):
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
        print(self.puzzle)


class Solver:
    def __init__(self, sud: Sudoku):
        self.sud = sud

    def solve(self, state: Sudoku, i=0, j=0):

        number_found = False

        for number in range(1, 10):
            if state.puzzle[i][j] == 0:
                if self.sud.check_if_number_ok(i, j, number):
                    number_found = True
                    state.puzzle[i][j] = number
                    if i == 8 and j == 8:
                        return True, state
                    elif j == 8:
                        solvable, ret_state = self.solve(state, i+1, 0)
                    else:
                        solvable, ret_state = self.solve(state, i, j+1)
                    if not solvable:
                        number_found = False
                        state.puzzle[i][j] = 0
                        continue
                    else:
                        return True, ret_state
            else:
                number_found = True
                if i == 8 and j == 8:
                    return True, state
                elif j == 8:
                    return self.solve(state, i + 1, 0)
                else:
                    return self.solve(state, i, j + 1)

        if not number_found:
            return False, state


if __name__ == "__main__":
    sud = Sudoku()
    sud.generate(20)
    sud.visualize()

    print("\n\n")

    solv = Solver(sud)
    solvable, solution = solv.solve(sud)
    if solvable:
        solution.visualize()
    else:
        print("Not solvable")

    assert len(sud.puzzle) == 9
    assert len(sud.puzzle[0]) == 9
