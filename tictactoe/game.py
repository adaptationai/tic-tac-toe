import random

import numpy as np

from . import DQN, AIPlayer, Player, RandomPlayer, State


class Play_game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
        self.current_state = State()
        self.current_player = None
        self.previous_player = None
        self.winner = "Draw"
        self.state_size = 9
        self.action_size = 9
        self.draw = 0
        self.batch_size = 32
        self.reward = 0
        self.symbol = 0
        return

    
    
    def play_full_step(self):
        self.setup(RandomPlayer(), AIPlayer(
            DQN(self.current_state, self.state_size, self.action_size, 0.01, False)))
        # self.player_two.agent.load_model("drive/tictactoe/tictactoemodel1.h5")
        # self.player_two.agent.load_target("drive/tictactoe/tictactoetarget1.h5")
        # self.player_two.agent.load_memory("drive/tictactoe/ticdeque1.pkl")
        games = 100000
        played = 0
        total = 0
        done = False
        target_update = 0

        for i in range(games):
            state = self.env.reset()
            done = False
            #print(f'new start{state}')
            for a in range(5000):
                
                state = np.reshape(state, [1, self.env.state_size])
                action = self.agent.act(state)
                new_state, reward, done = self.env.step(action)
               #print(f' state {state} action: {action} reward: {reward} new_state: {new_state} done:{done}')
                new_state = np.reshape(state, [1, self.env.state_size])

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
                    "tictactoe/data/tictactoemodel.h5")
                self.agent.save_target(
                    "tictactoe/data/tictactoetarget.h5")
                self.agent.save_memory(
                    "tictactoe/data/ticdeque.pkl")

        print(f' {self.env.winner} Wins')
        print(
            f' Scores:\n Player One: {self.env.player_one.score} \n Player Two:{self.env.player_two.score}  \n Draws:{self.env.draw}%')
        
        print('Good Bye')

  