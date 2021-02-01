import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_sudoku.envs.sudoku import Sudoku
import numpy as np


class SudokuEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self._n_filled_cells = 40
        self.reset()
        # we have 9 numbers that can be filled in a cell and 4 movements up,down,right,left to shift cells
        self.action_space = spaces.Discrete(9+4)
        self.observation_space = spaces.Box(low=np.array([0]*(9*9+2)), # 9*9 cells and 2 coordinates
                                            high=np.array([9]*9*9+[8,8]))

    @property
    def state(self):
        return np.append(self.sudoku.puzzle.flatten(), self.fill_pointer)

    def step(self, action):
        if action < 9:
            if self.sudoku.puzzle[self.fill_pointer[0], self.fill_pointer[1]] == 0 and self.sudoku.check_if_number_ok(self.fill_pointer[0], self.fill_pointer[1], action + 1):
                self.sudoku.puzzle[self.fill_pointer[0], self.fill_pointer[1]] = action + 1
            else:
                return self.state, 0, True, {}
        elif action == 9: # down
            if self.fill_pointer[0] < 9:
                self.fill_pointer[0] += 1
        elif action == 10: # up
            if self.fill_pointer[0] > 0:
                self.fill_pointer[0] -= 1
        elif action == 11: # right
            if self.fill_pointer[1] < 9:
                self.fill_pointer[1] += 1
        elif action == 12: # left
            if self.fill_pointer[1] > 0:
                self.fill_pointer[1] -= 1

        if not np.any(self.sudoku.puzzle == 0):
            return self.state, 1, True, {}
        return self.state, 0, False, {}

    def reset(self):
        self.sudoku = Sudoku()
        self.sudoku.generate(self._n_filled_cells)
        self.fill_pointer = np.array([0, 0])

    def render(self, mode='human'):
        print(self.sudoku.puzzle)



