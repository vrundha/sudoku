# Sudoku

Sudoku OpenAI gym for general purpose or Reinforcement Learning approaches.

# Sudoku Usage
Solving generated sudoku using backtracking
```py
from gym_sudoku.envs.sudoku import Sudoku
from gym_sudoku.envs.solver import Solver

sud = Sudoku()

# First, let us generate a random sudoku.

# The number of elements to be filled can be passed as a parameter. Let us visualse the generated sudoku.
sud.generate(22)
sud.visualize()

# Using Solver, let us solve this puzzle. A generated sudoku is always solvable.
solv = Solver(sud)
solvable, solution = solv.solve(sud)
sud.visualize()
```
This should print 
```
[5, 6, 2, 1, 4, 8, 7, 3, 9]
[8, 1, 4, 7, 3, 9, 2, 5, 6]
[7, 3, 9, 2, 5, 6, 8, 1, 4]
[4, 9, 5, 3, 7, 1, 6, 2, 8]
[3, 2, 7, 6, 8, 5, 4, 9, 1]
[1, 8, 6, 9, 2, 4, 5, 7, 3]
[2, 4, 8, 5, 1, 3, 9, 6, 7]
[6, 5, 3, 8, 9, 7, 1, 4, 2]
[9, 7, 1, 4, 6, 2, 3, 8, 5]
```

You can set your own puzzle as a 2d array to `Sudoku::puzzle`

# Gym Usage 
```py
from gym_sudoku.envs.sudoku_env import SudokuEnv

sudoku = SudokuEnv
print(sudoku.action_space) # Discrete(13)
print(sudoku.observation_space) # Box(0.0, 9.0, (83,), float32)

```
Rest of the usage can be found in [sudoku_env.py](gym_sudoku/envs/sudoku_env.py)


# Using DQN to solve sudoku
Here we used stable-baselines3 for this
```bash
python dqn_sudoku.py --train
```
