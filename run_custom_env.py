import gym
from custom_env import CustomEnv

# Create the environment
env = CustomEnv()

# Reset the environment and get the initial state
state = env.reset()

done = False
total_reward = 0

while not done:
    # Randomly choose an action
    action = env.action_space.sample()

    # Take a step in the environment
    next_state, reward, done, info = env.step(action)

    # Print the results
    print(f"Action: {action}, Reward: {reward}, State: {next_state}")

    total_reward += reward

# Final reward after the episode
print(f"Total reward: {total_reward}")

