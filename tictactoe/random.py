import numpy as np
import random


class RandomPlayer:
    def __init__(self):
        #self.agent = agent
    
        self.symbol = None
        self.current_state = None
        self.score = 0
        self.name = "Random Player"
        self.state_size = 9
        self.action_size = 9
        self.action = None
        self.reward = 0
        return

    def set_symbol(self, symbol):
        self.symbol = symbol
        return

    def take_action(self, current_state):
        # print(self.name)
        state = current_state
        #print(f'in: {state}')
        move = random.randrange(self.action_size)
        move = int(move)

        r = move // 3
        c = move % 3

        if state[r, c] != 0:
            
            return self.take_action(state)

        else:
            return (r, c, self.symbol)


    def feed_state(self, state):
        self.current_state = state
        return

    def feed_score(self, scores):
        self.score += scores

        return

    def feed_reward(self, reward):
        self.reward = reward
        return
