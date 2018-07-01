import numpy as np
import random


class AIPlayer:
    def __init__(self, agent):
        self.agent = agent
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

    def take_act(self, current_state):
        state = np.array(current_state.board)
        temp_board = np.array(current_state.board)

        state = np.reshape(state, [1, 9])

        argmax = self.agent.act(state)
        r = argmax // 3
        c = argmax % 3

        move = argmax

        if current_state.board[r, c] != 0:
            argsort = self.agent.act2(state)

            return self.valid_move(temp_board, argsort)

        else:

            return move

    def take_act_2(self, current_state):
        state = np.array(current_state.board)
        temp_board = current_state
        state = np.reshape(state, [1, 9])

        argmax = self.agent.act(state)
        r = argmax // 3
        c = argmax % 3
        move = argmax
        while temp_board.board[r, c] != 0:
            argmax = self.agent.act(state)
            r = argmax // 3
            c = argmax % 3

        return argmax

    def valid_move(self, state, argsort):
        temp_board = state

        for i in argsort:
            r = i // 3
            c = i % 3
            #print(f' i: {i}')
            if temp_board[r, c] == 0:
                #print(f' argsort valid: {i}')
                return i

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
