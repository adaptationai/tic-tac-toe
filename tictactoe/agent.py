import numpy as np
import random


class Agent:
    def __init__(self, ):
        #self.agent = agent
        self.symbol = None
        self.current_state = None
        self.score = 0
        self.name = "AIPlayer"
        self.state_size = 9
        self.action_size = 9
        self.action = None
        self.reward = 0
        self.skip = 0

        return

    def set_symbol(self, symbol):
        self.symbol = symbol
        return

    def take_action(self, action):

        move = action

        r = move // 3
        c = move % 3

        return (r, c, self.symbol)


    def random(self, move):
        action = random.randrange(self.action_size)
        while action == move:
            action = random.randrange(self.action_size)

        return action

    def feed_state(self, state):
        self.current_state = state
        return

    def feed_score(self, scores):
        self.score += scores

        return

    def feed_reward(self, reward):
        self.reward = reward
        return