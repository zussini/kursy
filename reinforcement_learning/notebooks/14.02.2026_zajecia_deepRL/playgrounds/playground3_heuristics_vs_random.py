import gymnasium as gym
import numpy as np

#sigmoid
def sigmoid(z):
    return 1.0/(1.0 + np.exp(-z))

#cechy
def phi(obs):
    x,xdot,th,thdot= obs
    return np.array([th,thdot],dtype=np.float32)

#losowa inicjalizacja wag
w = np.random.randn(2) * 0.1
print("initial w:",w)
w = np.array([1.0, 0.25])

#jedna gra z polityka parametryczna
env= gym.make("CartPole-v1")
obs,info = env.reset(seed=0)

total = 0

for t in range(500):
    features = phi(obs)
    z = np.dot(w, features)
    p = sigmoid(z)

    action = 1 if np.random.rand() <  p else 0
    #action = 1 if z >  0 else 0

    obs,reward,terminated,truncated, info = env.step(action)

    total+=reward

    if terminated or truncated:
        break

env.close()
print("return =",total)
