from gym_sudoku.envs.sudoku import Sudoku


class Solver:
    """
    Class to solve sudoku with backtracking
    """
    def __init__(self, sudoku: Sudoku):
        """
        
        :param sudoku: 
        """
        self.sudoku = sudoku

    def solve(self, state: Sudoku, i=0, j=0):
        """
        :param state: object of type Sudoku
        :param i: row index
        :param j: column index
        :return: tuple representing a boolean value to indicate if it is solved and the solved state
        """

        number_found = False

        for number in range(1, 10):
            if state.puzzle[i][j] == 0:
                if self.sudoku.check_if_number_ok(i, j, number):
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