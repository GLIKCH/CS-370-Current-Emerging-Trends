# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:57:44 2023
  5-1 Assignment: Cartpole Problem
            Joel De Alba
  Southern New Hampshire University
      Professor Timothy Alexander
              08 / 06 / 23
              
     Implementation Revision 10
     
     States in the CartPole implementation
     are as follows:
         - Cart Position x (x)
         - Cart Velocity ẋ (x Dot)
         - Pole Angle 	θ (Theta - Angle of Rotation)
         - Pole Velocity θ (Theta Dot - Angular Velocity )
"""


import gym
import numpy as np
import time

""" 
render_mode = 'human' provides for
a visual rendering animation of 
the CartPole Problem.

In this first code we are creating the
initial learning environment.
"""
env = gym.make('CartPole-v1', render_mode = 'human')

# Define exploration parameters
EXPLORATION_MAX = 1.0
EXPLORATION_MIN = 0.01
EXPLORATION_DECAY = 0.995

# Define other parameters
GAMMA = 0.99
LEARNING_RATE = 0.01  # Experiment with different learning rates

# Initialize Q-table
action_space_size = env.action_space.n
state_space_size = env.observation_space.shape[0]
q_table = np.zeros((state_space_size, action_space_size))


""" 
Other Practice Modifications

# Define exploration parameters
EXPLORATION_MAX = 1.0
EXPLORATION_MIN = 0.01
EXPLORATION_DECAY = 0.995

# Define other parameters
GAMMA = 0.9  # Experiment with different discount factors
LEARNING_RATE = 0.001

# Initialize Q-table
action_space_size = env.action_space.n
state_space_size = env.observation_space.shape[0]
q_table = np.zeros((state_space_size, action_space_size))

---------------------------------------------------------

# Define exploration parameters
EXPLORATION_MAX = 1.0  # Initial exploration probability
EXPLORATION_MIN = 0.01  # Minimum exploration probability
EXPLORATION_DECAY = 0.995  # Decay rate of exploration probability

# Define other parameters
GAMMA = 0.99  # Discount factor
LEARNING_RATE = 0.001  # Learning rate

# Initialize Q-table
action_space_size = env.action_space.n
state_space_size = env.observation_space.shape[0]
q_table = np.zeros((state_space_size, action_space_size))

"""

"""
Resets the environment and returns
to the initial state.
"""
(state, initial_state) = env.reset()

# Rendering the Environment
env.render()

# Closing the Environment
# env.close()

# Moving the Cart in One Direction
env.step(0)

# Observation Space Limits
env.observation_space
print("Observation Space -", env.observation_space, "\n")


# Observation Space Upper Limit
env.observation_space.high
print("Observation Space (High Limit) -", env.observation_space.high, "\n")


# Observation Space Lower Limit
env.observation_space.low
print("Observation Space (Low Limit) -", env.observation_space.low, "\n")

# Action Space
env.action_space
print("Action Space -", env.action_space, "\n")

# Review all specifications
env.spec
print("Specifications -", env.spec, "\n")

# Max Number of Steps per Episode
env.spec.max_episode_steps
print("# of Steps per Episode -", env.spec.max_episode_steps, "\n")

# Reward Threshold per Episode
env.spec.reward_threshold
print("Reward Threshhold -", env.spec.reward_threshold, "\n")

# Simulating the Environment
episodeNumber = 10000
timeSteps = 100

""" For each episode, the environment is reset,
    the current episide index is printed to
    the console, a new render is started, 
    observations are made, information on
    the environment and movement is created,
    and learning is perforemed by timesteps
    and observations made based on actions.
"""

for episodeIndex in range(episodeNumber):
    initial_state = env.reset()
    print(episodeIndex)
    env.render()
    appendedObservations = []
    for timeIndex in range(timeSteps):
        print(timeIndex)
        random_action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(random_action)
        appendedObservations.append(observation)
        time.sleep(0.01)
        if (terminated):
            time.sleep(3)
            break
        
env.close()

