import gym

env = gym.make('CartPole-v0') #setting up the environment

print('Initial observation')
observation = env.reset()
print(observation)

for _ in range(2): #rendering the environement 1000 times

    action = env.action_space.sample()

    observation, reward, done, info = env.step(action) 

    print('Observation')
    print(observation)
    print('\n')

    print('Reward')
    print(reward)
    print('\n')

    print('Done')
    print(done)
    print('\n')

    print('Info')
    print(info)
    print('\n')





'''
    Observation - Environement specific info.Ex. Angle, Velocities, Game states etc.

    Reward - Amount of reward achieved by previous action. Scale varies based off environment but agent should always want to increase reward level

    Done - Boolean indicating whether environ needs to be reset. Ex Game lost

'''