import random

import numpy as np

from . import DQN, AIPlayer, Player, RandomPlayer, State 

class Play():
    def __init__(self):
        self.test = None
    
    def training(self):
        self.env = State()
        state = self.env.setup()
        self.agent = DQN(self.env, self.env.state_size, self.env.action_size, 0.0, True)
        games = 10000000
        played = 0
        total = 0
        done = False
        target_update = 0

        for i in range(games):
            state = self.env.reset()
            done = False
            #print(f'new start{state}')
            for a in range(5000):
                state =  np.copy(self.env.current_state)
                state = np.reshape(state, [1, self.env.state_size])
                #print(f'step state{state}')
                action = self.agent.act(state)
                new_state, reward, done = self.env.step(action)
                
                new_state = np.reshape(new_state, [1, self.env.state_size])
                #print(f' state {state} action: {action} reward: {reward} new_state: {new_state} done:{done}')

                self.agent.remember(
                    state, action, reward, new_state, done)
                self.agent.replay()
                target_update += 1
                if target_update > 1000:
                    self.agent.target_train()
                    target_update = 0
                if done:
                    break

            played += 1
           
            total += 1
            if played >= 100:
                # self.current_state.render()
                percent = self.env.player_one.score / total * 100
                # clear_output()
                
                print(
                    f' Games played: {total}\n Scores:\n Player One: {self.env.player_one.score} \n Player Two:{self.env.player_two.score}  \n Draws:{self.env.draw} \n Percentage: {percent}')
                played = 0
                print(self.agent.epsilon)
                print(target_update)
                self.agent.save_model(
                    "tictactoe/data/tictactoemodel2.h5")
                self.agent.save_target(
                    "tictactoe/data/tictactoetarget2.h5")
                self.agent.save_memory(
                    "tictactoe/data/ticdeque2.pkl")

        print(f' {self.env.winner} Wins')
        print(
            f' Scores:\n Player One: {self.env.player_one.score} \n Player Two:{self.env.player_two.score}  \n Draws:{self.env.draw}%')
        
        print('Good Bye')