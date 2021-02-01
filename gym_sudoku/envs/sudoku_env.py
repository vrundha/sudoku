import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_sudoku.envs.sudoku import Sudoku
import numpy as np


class SudokuEnv(gym.Env):
    """
    Gym for sudoku.
    The action space consists of the 9 actions to fill numbers 1 to 9 in the cell and 4 actions to move up, down, left, right in the puzzle.
    The observation space consists of 81 cells of the puzzle and 2 indices of the pointer.
    """
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self._n_filled_cells = 10
        self.reset(regenerate=True)
        # we have 9 numbers that can be filled in a cell and 4 movements up,down,right,left to shift cells
        self.action_space = spaces.Discrete(9+4)
        self.observation_space = spaces.Box(low=np.array([0]*(9*9+2)),# 9*9 cells and 2 coordinates
                                            high=np.array([9]*9*9+[8,8]))

    @property
    def state(self):
        """
        State of the environment which has the puzzle and the indices of the pointer.
        :return: state
        """
        return np.append(self.sudoku.puzzle.flatten(), self.fill_pointer)

    def step(self, action):
        """
        Run one timestep of the environment's dynamics. When end of
        episode is reached, you are responsible for calling `reset()`
        to reset this environment's state.

        Accepts an action and returns a tuple (observation, reward, done, info).
        :param action: an action provided by the agent
        :return: observation, reward, done, info

        """
        if action < 9:
            if self.sudoku.puzzle[self.fill_pointer[0], self.fill_pointer[1]] == 0 and self.sudoku.check_if_number_ok(self.fill_pointer[0], self.fill_pointer[1], action + 1):
                self.sudoku.puzzle[self.fill_pointer[0], self.fill_pointer[1]] = action + 1
            else:
                return self.state, 0, True, {}
        else:
            if action == 9:  # down
                if self.fill_pointer[0] < 8:
                    self.fill_pointer[0] += 1
                else:
                    return self.state, 0, True, {}
            elif action == 10:  # up
                if self.fill_pointer[0] > 0:
                    self.fill_pointer[0] -= 1
                else:
                    return self.state, 0, True, {}
            elif action == 11:  # right
                if self.fill_pointer[1] < 8:
                    self.fill_pointer[1] += 1
                else:
                    return self.state, 0, True, {}
            elif action == 12:  # left
                if self.fill_pointer[1] > 0:
                    self.fill_pointer[1] -= 1
                else:
                    return self.state, 0, True, {}

        if not np.any(self.sudoku.puzzle == 0):
            return self.state, 1, True, {}
        return self.state, 0, False, {}

    def reset(self, regenerate=False):
        """
        Resets the environment to an initial state and returns an initial
        observation.
        :param regenerate: boolean. If true, new puzzle is generated
        :return: new state
        """
        if regenerate:
            self.sudoku = Sudoku()
            self.sudoku.generate(self._n_filled_cells)
        self.fill_pointer = np.array([0, 0])
        return self.state

    def render(self, mode='human'):
        """
        Renders the environment.
        """
        print(self.sudoku.puzzle)



