import sys
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.dqn.policies import MlpPolicy
from stable_baselines3 import DQN
from gym_sudoku.envs.sudoku_env import SudokuEnv

env = SudokuEnv()

if "--train" in sys.argv:
    model = DQN(MlpPolicy, env, verbose=1, learning_starts=100)
    model.learn(total_timesteps=10000)
    model.save("dqn_sudoku")
else:
    model = DQN.load("dqn_sudoku")

obs = env.reset()
env.render()
for _ in range(20):
    action, _states = model.predict(obs, deterministic=True)
    print("Action", action)
    print("States", _states)
    print("Coordinates", env.fill_pointer)
    obs, rewards, done, info = env.step(action)
    env.render()
    if done:
        print("Resetting ==============================================>")
        obs = env.reset()

