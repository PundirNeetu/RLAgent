import gym
from gym import spaces
import numpy as np

class CustomEnv(gym.Env):
    def __init__(self):
        super(CustomEnv, self).__init__()
        
        # Action space: Example of a discrete action space
        # This means there are 3 possible actions (e.g., 0 = "Move Left", 1 = "Move Right", 2 = "Stay")
        self.action_space = spaces.Discrete(3)

        # Observation space: Example of a 1D space with values between 0 and 10
        # This is a simple state space, e.g., an agent's position between 0 and 10
        self.observation_space = spaces.Discrete(11)

        # Initial state
        self.state = 5  # Let's say the agent starts at position 5

    def reset(self):
        # Reset the environment state to its initial condition
        self.state = 5
        return self.state

    def step(self, action):
        # Update the state based on the action taken
        if action == 0:
            self.state -= 1  # Move left
        elif action == 1:
            self.state += 1  # Move right
        elif action == 2:
            pass  # Stay in place

        # Ensure the state stays within bounds (0 to 10)
        self.state = max(0, min(self.state, 10))

        # Define a simple reward: reach the state 10 (goal) to get a positive reward
        done = False
        if self.state == 10:
            done = True
            reward = 1  # Positive reward when reaching goal
        else:
            reward = -0.1  # Small negative reward to encourage reaching the goal

        # Return the observation, reward, done, and additional info
        return self.state, reward, done, {}

    def render(self):
        # Display the current state (e.g., position of the agent)
        print(f"Agent's position: {self.state}")
