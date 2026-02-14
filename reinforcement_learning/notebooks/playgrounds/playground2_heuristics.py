import gymnasium as gym 
import numpy as np
def run_policy(policy_fn, episodes=50, seed=0):
    env = gym.make("CartPole-v1")
    rets = []
    for ep in range(episodes):
        obs,info = env.reset(seed=seed+ep)
        total = 0
        while True:
            action = policy_fn(obs)
            obs,reward,terminated,truncated,info = env.step(int(action))
            total+=reward
            if terminated or truncated:
                break
        rets.append(total)
    env.close()
    return float(np.mean(rets)),float(np.std(rets))
def heur_theta(obs):
    x,xdot,th,thdot = obs
    return 1 if th> 0 else 0

print("theta-only mean\pm std:",*run_policy(heur_theta,episodes=50,seed=0))

#herystyka theta + c*thetadot

def make_heur_theta_dot(c):
    def policy(obs):
        x,xdot,th,thdot = obs
        u = th + c*thdot
        return 1 if u > 0 else 0 
    return policy

for c in [0.0,0.1,0.25,0.5,1.0]:
    mean,std = run_policy(make_heur_theta_dot(c),episodes=50, seed=0)
    print(f"c={c:>4} mean\pm std: {mean:6.1f} \pm {std:5.1f}")
