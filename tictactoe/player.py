import numpy as np


class Player:
    def __init__(self):
          #self.agent = agent
        self.symbol = None
        self.current_state = None
        self.score = 0
        self.name = "Player"
        self.state_size = 9
        self.action_size = 9
        self.action = None
        self.reward = 0
        return

    def set_symbol(self, symbol):
        self.symbol = symbol
        return

    def take_action(self, current_state):
        state = current_state
        move = 0
        while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            move = input('Please select your postition (1-9 from top left) ')
        move = int(move)
        move = move - 1
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
