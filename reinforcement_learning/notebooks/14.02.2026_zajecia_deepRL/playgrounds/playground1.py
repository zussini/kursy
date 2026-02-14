#losowa polityka
import gymnasium as gym
env = gym.make("CartPole-v1")
obs,info = env.reset(seed=0)
for t in range(200):
    x,xdot,th,thdot = obs

    if t%10==0:
        print(f"={t:3d} | x={x:+.3f} xdot={xdot:+3f} theta={th:+.3f} thetadot={thdot:+.3f}")
        if th * thdot > 0:
            print("   -> kij ucieka dalej (pogarsza się): theta i thetadot mają ten sam znak")
        elif th * thdot < 0:
            print("   -> kij wraca / hamuje przechył: theta i thetadot mają przeciwne znaki")
        else:
            print("   -> granicznie: theta*thetadot = 0 (rzadko)")
    action = env.action_space.sample()

    obs,reward,terminated,truncated,info = env.step(action)

    done = terminated or truncated

    if done:
        obs,info = env.reset()

#sredni return heurystyka
import gymnasium as gym
import numpy as np

def run_policy(policy_fn, episodes=20, seed=0):
    env = gym.make("CartPole-v1")
    rets = []
    for ep in range(episodes):
        obs, info = env.reset(seed=seed+ep)
        total = 0
        while True:
            action = policy_fn(obs)
            obs, reward, terminated, truncated, info = env.step(action)
            total += reward
            if terminated or truncated:
                break
        rets.append(total)
    env.close()
    return np.mean(rets), np.std(rets), rets

# 1) random
mean_r, std_r, _ = run_policy(lambda obs: np.random.randint(0,2), episodes=30)
print("RANDOM   mean±std:", mean_r, std_r)

# 2) heuristic: push towards the tilt
def heuristic(obs):
    x, xdot, th, thdot = obs
    return 1 if th > 0 else 0

mean_h, std_h, _ = run_policy(heuristic, episodes=30)
print("HEURISTIC mean±std:", mean_h, std_h)

        
