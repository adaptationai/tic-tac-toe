import numpy as np

from .player import Player
from .ai import AIPlayer
from .random import RandomPlayer
from .agent import Agent
import random


class State():
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.winner = None
        self.end = None
        self.current_state = None
        self.previous_state = None
        self.next_state = None
        self.current_player = None
        self.previous_player = None
        self.next_state = None
        self.player_one = None
        self.player_two = None
        self.state_size = 9
        self.action_size = 9
        self.draw = 0
        self.loop = 0
        return

    def move_ok(self, r, c):
        if self.current_state[r, c] != 0:
            return True
        else:
            return False

    def render(self):
        # clear_output()
        temp_board = self.current_state.tolist()
        for i in range(len(temp_board)):
            for j in range(len(temp_board)):
                if temp_board[i][j] == 1:
                    temp_board[i][j] = "O"
                if temp_board[i][j] == -1:
                    temp_board[i][j] = "X"
                elif temp_board[i][j] == 0.0:
                    temp_board[i][j] = "*"

        print(f' {temp_board[0][0]}|{temp_board[0][1]}|{temp_board[0][2]}\n-------\n {temp_board[1][0]}|{temp_board[1][1]}|{temp_board[1][2]}\n-------\n {temp_board[2][0]}|{temp_board[2][1]}|{temp_board[2][2]}')

    

    def checker(self):
        if self.end is not None:
            return self.end
        result = []
        # row check p1

        if self.current_state[0][0] == self.current_state[0][1] == self.current_state[0][2] == 1 or self.current_state[1][0] == self.current_state[1][1] == self.current_state[1][2] == 1 or self.current_state[2][0] == self.current_state[2][1] == self.current_state[2][2] == 1:
            self.end = True
            self.winner = 1
            return self.end

        # colums check p1
        if self.current_state[0][0] == self.current_state[1][0] == self.current_state[2][0] == 1 or self.current_state[0][1] == self.current_state[1][1] == self.current_state[2][1] == 1 or self.current_state[0][2] == self.current_state[1][2] == self.current_state[2][2] == 1:
            self.end = True
            self.winner = 1
            return self.end
        # crosses p1
        if self.current_state[0][0] == self.current_state[1][1] == self.current_state[2][2] == 1 or self.current_state[0][2] == self.current_state[1][1] == self.current_state[2][0] == 1:
            self.end = True
            self.winner = 1
            return self.end

        # row check p2
        if self.current_state[0][0] == self.current_state[0][1] == self.current_state[0][2] == -1 or self.current_state[1][0] == self.current_state[1][1] == self.current_state[1][2] == -1 or self.current_state[2][0] == self.current_state[2][1] == self.current_state[2][2] == -1:
            self.end = True
            self.winner = -1

            return self.end
        # colums check p2
        if self.current_state[0][0] == self.current_state[1][0] == self.current_state[2][0] == -1 or self.current_state[0][1] == self.current_state[1][1] == self.current_state[2][1] == -1 or self.current_state[0][2] == self.current_state[1][2] == self.current_state[2][2] == -1:
            self.end = True
            self.winner = -1
            return self.end
        # crosses p2
        # crosses p1
        if self.current_state[0][0] == self.current_state[1][1] == self.current_state[2][2] == -1 or self.current_state[0][2] == self.current_state[1][1] == self.current_state[2][0] == -1:
            self.end = True
            self.winner = -1
            return self.end

        # Draw check
        if self.current_state[0][0] != 0 and self.current_state[0][1] != 0 and self.current_state[0][2] != 0 and self.current_state[1][0] != 0 and self.current_state[1][1] != 0 and self.current_state[1][2] != 0 and self.current_state[2][0] != 0 and self.current_state[2][1] != 0 and self.current_state[2][2] != 0:
            self.winner = 0
            self.end = True
            return self.end

        return self.end



    def step(self, action):
        #print(f'player_one: {self.current_state}')
        self.current_player = self.player_one
        self.previous_player = self.player_two
        self.current_player.feed_state(self.current_state)
        r, c, symbol = self.current_player.take_action(action)
        if self.current_state[r,c] != 0:
            #print('moose')
           
            new_state = np.array(self.current_state)
            #new_state = np.reshape(new_state, [1, self.state_size])
            self.previous_player.feed_score(1)
            reward = -1
            #reward = self.iswin()
            #done = self.checker()
            done = True
            #print("yeah")
            return new_state, reward, done
            
        else:
            self.loop = 0
            self.current_state[r, c] = symbol
            #print(f'else current state = {self.current_state}')
            done = self.checker()
            reward = self.iswin()
            new_state = np.array(self.current_state)
            #new_state = np.reshape(new_state, [1, self.state_size])

            if done == True:
            # print("half")
                return new_state, reward, done
        
        self.render()     
        self.current_player = self.player_two
        self.previous_player = self.player_one
        self.current_player.feed_state(self.current_state)
        #state2 = np.array(self.current_state.board)
        #state2 = np.reshape(state2, [1, self.state_size])
        #print(f'Player_two: {self.current_state}')
        r, c, symbol = self.current_player.take_action(self.current_state)

        self.current_state[r, c] = symbol
        done = self.checker()
        reward = self.iswin()
        new_state = np.array(self.current_state)
        new_state = np.reshape(new_state, [1, self.state_size])
        #print(f'p2 current = {self.current_state}')
        #print(f'new state = {new_state}')

        return new_state, reward, done


    def setup(self):

        self.current_state = self.board
        self.player_one = Agent()
        self.player_two = RandomPlayer()
        #self.player_one = Agent()
        #self.player_two = Player()
        self.player_one.name = "Player One"
        self.player_two.name = "Player Two"
        self.player_one.symbol = 1
        self.player_two.symbol = -1
        self.player_one.feed_state(self.current_state)
        self.player_two.feed_state(self.current_state)
        return self.current_state

        #self.starter()

    def reset(self):
        self.resetting()
        self.current_state = self.board
        self.current_player = self.player_one
        self.previous_player = self.player_two
        self.symbol = 1
        #self.starter()
        self.winner = "Draw"
        self.reward = 0
        self.current_player.reward = 0
        self.previous_player.reward = 0

        return self.current_state

    def starter(self):
        if random.randint(0, 1) == 0:
            self.current_player = self.player_one
            self.previous_player = self.player_two
            self.symbol = 1
        else:
            self.current_player = self.player_two
            self.previous_player = self.player_one
            self.symbol = -1


    def iswin(self):

        if self.winner == self.current_player.symbol:
            self.winner = self.current_player.name
            self.current_player.feed_score(1)
            self.previous_player.feed_score(0)
            self.current_player.feed_reward(10)
            self.previous_player.feed_reward(0)
            if self.current_player.symbol == self.player_one.symbol:
                return 1
            else:
                return -1

        elif self.winner == 0:
            self.current_player.feed_score(0)
            self.previous_player.feed_score(0)
            self.current_player.feed_reward(0.1)
            self.previous_player.feed_reward(0.5)
            self.draw += 1
            self.winner = "Draw"
            if self.current_player.symbol == self.player_two.symbol:
                return 0.5
            if self.previous_player.symbol == self.player_two.symbol:
                return 0.1

        else:
            return 0

    def who_moves(self, current, previous):
        self.previous_player = current
        self.current_player = previous

    def resetting(self):
        self.board = np.zeros((3, 3))
        self.winner = None
        self.end = None
        self.current_state = None
        self.previous_state = None
        self.next_state = None
        self.current_player = None
        self.previous_player = None
        self.next_state = None
        self.loop = 0
        

        
