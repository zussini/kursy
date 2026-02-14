import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1.0/(1.0 +np.exp(-z))

def phi(obs):
    x,xdot,th,thdot = obs
    return np.array([th,thdot],dtype=np.float32)

def compute_returns(rewards,gamma=0.99):
    G=0.0
    out = []
    for r in reversed(rewards):
        G = r + gamma*G
        out.append(G)
    out.reverse()
    return np.array(out,dtype = np.float32)
def logpi_and_grad(w,features,action):
    z = float(np.dot(w,features))
    p = sigmoid(z)
    if action ==1:
        logp = np.log(p+1e-8)
    else:
        logp = np.log(1.0 - p + 1e-8)
    grad = (action - p ) * features
    return logp,grad,p,z

env = gym.make("CartPole-v1")
obs,info = env.reset(seed=0)
w = np.array([0.0,0.0],dtype =np.float32)
returns_hist = []

alpha = 0.01
gamma = 0.99
episodes = 400
baseline = 0.0
beta = 0.9

for ep in range(episodes):
    obs,info = env.reset(seed=ep)
    phi_list = []
    act_list = []
    rew_list = []
    total= 0.0
    for t in range(500):
        features = phi(obs)
        z = float(np.dot(w,features))
        p = sigmoid(z)
        action = 1 if np.random.rand() < p else 0
        next_obs,reward,terminated, truncated,info = env.step(action)
        done = terminated or truncated
        phi_list.append(features)
        act_list.append(action)
        rew_list.append(float(reward))
        total+=float(reward)

        obs = next_obs
        if done:
            break
    print("Episode return(length):", total)

    G = compute_returns(rew_list, gamma=gamma)
    #baseline aktualizacja  - EMA - exp moving averages - baseline = beta*baseline + (1-beta)*G0
    baseline = beta*baseline + (1 - beta)*float(G[0])
    grad_sum = np.zeros_like(w)
    for t in range(len(G)):
        logp, grad_logp,p,z = logpi_and_grad(w, phi_list[t],act_list[t])
        advantage = G[t] - baseline
        grad_sum+=grad_logp*advantage
    update=alpha*grad_sum
    w_new = w+update
    w = w_new
    returns_hist.append(total)
    if (ep + 1) % 50 == 0:
        avg = np.mean(returns_hist[-50:])
        print(f"ep {ep+1:4d} | avg_return(last50)={avg:6.1f} | w={w} | baseline={baseline:.1f}")
env.close()

# wykres
def moving_average(x, window=20):
    x = np.asarray(x, dtype=float)
    if len(x) < window:
        return x
    return np.convolve(x, np.ones(window)/window, mode='valid')
plt.figure(figsize=(9,4))
plt.plot(returns_hist, alpha=0.4, label="return")
plt.plot(range(19, 19+len(moving_average(returns_hist, 20))), moving_average(returns_hist, 20), label="MA20")
plt.title("REINFORCE (linear policy): CartPole returns")
plt.xlabel("episode")
plt.ylabel("return")
plt.legend()
plt.show()
print("final w:", w)
