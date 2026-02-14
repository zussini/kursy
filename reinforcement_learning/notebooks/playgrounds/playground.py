import gymnasium as gym
env = gym.make("CartPole-v1",render_mode="human")
obs,info = env.reset()
print(obs,obs.shape,info)
action = env.action_space.sample()
obs,reward,terminated,truncated,info = env.step(action)
done = terminated or truncated
#terminated - epizod skonczony, np. kij upadl poza rog
# truncated - epizod uciety - limit czasu/krokow
# done = terminated or truncated - do petli

print(env.observation_space)



#3!
print(env.action_space)
print("obs_dim=", env.observation_space.shape[0])
print("n_actions =", env.action_space.n)
#action - dwie , observation space - 4dim

#4!
obs,info = env.reset()
total = 0
for t in range(500):
    action = env.action_space.sample()
    obs,reward,terminated,truncated, info = env.step(action)
    total+=reward
    if terminated or truncated:
        break
print("return =", total,  "steps =", t+1)
env.close()

#x - polozenie wozka, dot{x} - predkosc wozka, theta - kat drazka wzgledem pionu, dot{theta} - predkosc katowa drazka
#rgb_array 
#
env = gym.make("CartPole-v1", render_mode = "rgb_array")
obs,info=env.reset()
frame = env.render()
print(frame.shape)
env.close()

#5!
#A
env = gym.make("CartPole-v1",render_mode="human")
obs,info = env.reset()
for _ in range(200):
    action = env.action_space.sample()
    obs,reward,terminated,truncated, info = env.step(action)
    if terminated or truncated:
        obs,info = env.reset()
env.close()
#B
env = gym.make("CartPole-v1", render_mode="rgb_array")
obs,info = env.reset()
frame = env.render()
print(frame.shape)
env.close()

#6!
obs,info = env.reset(seed=0)
env.action_space.seed(0)

