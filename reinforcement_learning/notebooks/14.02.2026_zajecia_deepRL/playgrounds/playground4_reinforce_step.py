import gymnasium as gym
import numpy as np

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

alpha = 0.05
gamma = 0.99
baseline = 0.0

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

env.close()
print("Episode return(length):", total)
G = compute_returns(rew_list, gamma=gamma)
grad_sum = np.zeros_like(w)
for t in range(len(G)):
    logp, grad_logp,p,z = logpi_and_grad(w, phi_list[t],act_list[t])
    advantage = G[t] - baseline
    grad_sum+=grad_logp*advantage

update=alpha*grad_sum
w_new = w+update
print("w before:",w)
print("update :",update)
print("w after :",w_new)

print("\nFirst 5 steps:")
for i in range(min(5,len(G))):
    z = float(np.dot(w,phi_list[i]))
    p = sigmoid(z)
    print(f"t={1:2d} a={act_list[i]} p={p:.3f} G={G[i]:.2f} phi={phi_list[i]}")
