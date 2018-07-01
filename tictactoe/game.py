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

    def starter(self):
        if random.randint(0, 1) == 0:
            self.current_player = self.player_one
            self.previous_player = self.player_two
            self.symbol = 1
        else:
            self.current_player = self.player_two
            self.previous_player = self.player_one
            self.symbol = -1

    def setup(self, player_one, player_two):
        self.current_state = State()
        self.player_one = player_one
        self.player_two = player_two
        self.player_one.name = "Player One"
        self.player_two.name = "Player Two"
        self.player_one.symbol = 1
        self.player_two.symbol = -1
        self.player_one.feed_state(self.current_state)
        self.player_two.feed_state(self.current_state)
        # self.player_two.agent.load("drive/tictactoe/tictactoemodelfixedneg.h5")
        # self.player_two.agent.load_target("drive/tictactoe/tictactoetargetfixedneg.h5")
        # self.player_one.agent.load("drive/tictactoe/tictactoemodelfizedneg.h5")
        # self.player_one.agent.load_target("drive/tictactoe/tictactoetargetfixedneg.h5")
        # self.player_two.agent.save("drive/tictactoe/tictactoemodelfixedfinal2duel.h5")
        # self.player_two.agent.save_target("drive/tictactoe/tictactoetargetfixedfinal2duel.h5")

        self.starter()

    def reset(self):
        self.current_state = State()
        #self.current_player = self.player_two
        #self.previous_player = self.player_one
        self.starter()
        self.winner = "Draw"
        self.reward = 0
        self.current_player.reward = 0
        self.previous_player.reward = 0

        return

    def reset2(self):
        self.current_state = State()
        self.current_player = self.player_two
        self.previous_player = self.player_one
        self.winner = "Draw"
        self.reward = 0
        return

    def welcome_screen(self):
        print("Welcome to TicTacToe")
        response = None
        while response != 'yes' or response != 'no':
            response = input("Would you like to play a game, 'yes' or 'no'?")
            response.lower()
            if response == 'yes':
                return True
            elif response == 'no':
                return False

    def who_moves(self):
        current = self.previous_player
        previous = self.current_player
        return current, previous

    def iswin(self):

        if self.current_state.winner == self.current_player.symbol:
            self.winner = self.current_player.name
            self.current_player.feed_score(1)
            self.previous_player.feed_score(0)
            self.current_player.feed_reward(10)
            self.previous_player.feed_reward(0)
            if self.current_player.symbol == self.player_two.symbol:
                return 1
            else:
                return -1

        elif self.current_state.winner == 0:
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
        #observation, reward, self.current_state.done= self.step(self.current_player.take_action())

    def finish(self):
        response = None
        while response != 'yes' or response != 'no':
            response = input("Would you like to play again, 'yes' or 'no'?")
            response.lower()
            if response == 'yes':
                return True
            elif response == 'no':
                return False

    def step2(self, action):

        self.current_player = self.player_two
        self.previous_player = self.player_one
        self.current_player.feed_state(self.current_state)
        r, c, symbol = self.current_player.take_action(action)
        self.current_state.board[r, c] = symbol
        done = self.current_state.checker2()
        reward = self.iswin()
        new_state = np.array(self.current_state.board)
        new_state = np.reshape(new_state, [1, self.state_size])

        if done == True:
            # print("half")
            return new_state, reward, done
        # self.current_state.render()
        self.current_player = self.player_one
        self.previous_player = self.player_two
        self.current_player.feed_state(self.current_state)
        #state2 = np.array(self.current_state.board)
        #state2 = np.reshape(state2, [1, self.state_size])
        r, c, symbol = self.current_player.take_action()

        self.current_state.board[r, c] = symbol
        done = self.current_state.checker2()
        reward = self.iswin()
        new_state = np.array(self.current_state.board)
        new_state = np.reshape(new_state, [1, self.state_size])

        return new_state, reward, done

    def step3(self, action):

        self.current_player = self.player_two
        self.previous_player = self.player_one
        self.current_player.feed_state(self.current_state)
        r, c, symbol = self.current_player.take_action()
        self.current_state.board[r, c] = symbol
        # print("before")
        done = self.current_state.checker2()
        # print("after")
        reward = self.iswin()
        new_state = np.array(self.current_state.board)
        new_state = np.reshape(new_state, [1, self.state_size])

        if done == True:
            # print("half")
            return new_state, reward, done

        self.current_player = self.player_one
        self.previous_player = self.player_two
        self.current_player.feed_state(self.current_state)
        #state2 = np.array(self.current_state.board)
        #state2 = np.reshape(state2, [1, self.state_size])
        action2 = self.current_player.take_act_2(self.current_state)
        r, c, symbol = self.current_player.take_action(action2)

        self.current_state.board[r, c] = symbol
        done = self.current_state.checker2()
        reward = self.iswin()
        new_state = np.array(self.current_state.board)
        new_state = np.reshape(new_state, [1, self.state_size])

        return new_state, reward, done

    def play_full_step(self):
        self.setup(RandomPlayer(), AIPlayer(
            DQN(self.current_state, self.state_size, self.action_size, 1.0, False)))
        # self.player_two.agent.load_model("drive/tictactoe/tictactoemodel1.h5")
        # self.player_two.agent.load_target("drive/tictactoe/tictactoetarget1.h5")
        # self.player_two.agent.load_memory("drive/tictactoe/ticdeque1.pkl")
        games = 100000
        played = 0
        total = 0
        done = False
        target_update = 0

        for i in range(games):
            self.reset()
            done = False
            if self.symbol == self.player_one.symbol:
                self.current_player = self.player_one
                self.previous_player = self.player_two
                self.current_player.feed_state(self.current_state)
                r, c, symbol = self.current_player.take_action()
                self.current_state.board[r, c] = symbol
                done = self.current_state.checker()
                reward = self.iswin()

                new_state = np.array(self.current_state.board)
                new_state = np.reshape(new_state, [1, self.state_size])

                self.symbol = 0
                self.current_player = self.player_two
                self.previous_player = self.player_one

            for a in range(5000):

                # self.current_state.render()

                state = np.array(self.current_state.board)
                state = np.reshape(state, [1, self.state_size])

                # print(state)
                action = self.player_two.take_act_2(self.current_state)
                #state =numpy.array(state)
                # print(action)
                # print(state)
                new_state, reward, done = self.step2(action)
                # print(state)
                #print(f' state {state} action: {action} reward: {reward} new_state: {new_state} done:{done}')
                new_state = np.reshape(state, [1, self.state_size])
                self.player_two.agent.remember(
                    state, action, reward, new_state, done)
                self.player_two.agent.replay()
                target_update += 1
                if target_update > 10000:
                    self.player_two.agent.target_train()
                    target_update = 0
                if done:
                    break

            played += 1
            # self.current_state.render()
            #print(f' {self.winner} Wins')
            # clear_output()
            #print(f' total played: {total}')
            total += 1
            if played >= 100:
                # self.current_state.render()
                percent = self.player_two.score / total * 100
                # clear_output()
                # self.current_state.render
                print(
                    f' Games played: {total}\n Scores:\n Player One: {self.player_one.score} \n Player Two:{self.player_two.score}  \n Draws:{self.draw} \n Percentage: {percent}')
                played = 0
                print(self.player_two.agent.epsilon)
                print(target_update)
                self.player_two.agent.save_model(
                    "tictactoe/data/tictactoemodel.h5")
                self.player_two.agent.save_target(
                    "tictactoe/data/tictactoetarget.h5")
                self.player_two.agent.save_memory(
                    "tictactoe/data/ticdeque.pkl")

        print(f' {self.winner} Wins')
        print(
            f' Scores:\n Player One: {self.player_one.score} \n Player Two:{self.player_two.score}  \n Draws:{self.draw}%')
        #print(f' state {state} action: {action} reward: {reward} new_state: {new_state} done:{done}')
        #new_state = np.reshape(state, [1, self.state_size])
        # self.player_two.agent.save_model("success.model")

        # self.player_two.agent.save("drive/tictactoe/tictactoemodelfixedfinal2.h5")
        # self.player_two.agent.save_target("drive/tictactoe/tictactoetargetfixedfinal2.h5")
        # self.player_two.agent.save("drive/tictactoe/tictactoemodelfixedfinal200k.h5")
        # self.player_two.agent.save_target("drive/tictactoe/tictactoetargetfixedfinal200k.h5")
        print('Good Bye')

    def play_full_step_trained(self):

        self.setup(AIPlayer(DQN(self.current_state, self.state_size, self.action_size, 0.01)), AIPlayer(
            DQN(self.current_state, self.state_size, self.action_size, 1.0)))

        self.player_two.agent.load(
            "drive/tictactoe/tictactoemodelfixed200k2.h5")
        self.player_two.agent.load_target(
            "drive/tictactoe/tictactoetargetfixed2002k.h5")
        self.player_one.agent.load(
            "drive/tictactoe/tictactoemodelfixed200k2.h5")
        self.player_one.agent.load_target(
            "drive/tictactoe/tictactoetargetfixed2002k.h5")

        games = 10000
        played = 0
        total = 0
        done = False
        target_update = 0

        for i in range(games):
            self.reset()
            done = False
            if self.symbol == self.player_one.symbol:
                # self.current_state.render()
                self.current_player = self.player_one
                self.previous_player = self.player_two
                self.current_player.feed_state(self.current_state)
                #state =np.array(self.current_state.board)
                #state = np.reshape(state, [1, self.state_size])
                action2 = self.current_player.take_act_2(self.current_state)
                r, c, symbol = self.current_player.take_action()

                self.current_state.board[r, c] = symbol
                #done = self.current_state.checker()
                #reward = self.iswin()

                #new_state = np.array(self.current_state.board)
                #new_state = np.reshape(new_state, [1, self.state_size])

                self.symbol = 0
                self.current_player = self.player_two
                self.previous_player = self.player_one

            for a in range(100000):

                # self.current_state.render()

                state = np.array(self.current_state.board)
                state = np.reshape(state, [1, self.state_size])

            # print(state)
                action = self.player_two.take_act(self.current_state)
            #state =numpy.array(state)
            # print(action)
            # print(state)
                new_state, reward, done = self.step3(action)
            # print(state)
                #print(f' state {state} action: {action} reward: {reward} new_state: {new_state} done:{done}')
                new_state = np.reshape(state, [1, self.state_size])
                # self.current_state.render
                self.player_two.agent.remember(
                    state, action, reward, new_state, done)
                self.player_two.agent.replay()
                target_update += 1
                if target_update > 1000:

                    self.player_two.agent.target_train()
                    target_update = 0
                if done:
                    # self.current_state.render
                    break

            played += 1

            # clear_output()
            #print(f' total played: {total}')
            total += 1
            if played >= 100:
                # self.current_state.render()
                percent = self.player_two.score / total * 100
                # clear_output()
                # self.current_state.render
                print(
                    f' Games played: {total}\n Scores:\n Player One: {self.player_one.score} \n Player Two:{self.player_two.score}  \n Draws:{self.draw} \n Percentage: {percent}')
                played = 0
                print(self.player_two.agent.epsilon)
                # self.current_state.render()
                self.player_two.agent.save(
                    "drive/tictactoe/tictactoemodelfixedfinal21duel.h5")
                self.player_two.agent.save_target(
                    "drive/tictactoe/tictactoetargetfixedfinal21duel.h5")

        print(f' {self.winner} Wins')
        print(
            f' Scores:\n Player One: {self.player_one.score} \n Player Two:{self.player_two.score}  \n Draws:{self.draw}%')
        #print(f' state {state} action: {action} reward: {reward} new_state: {new_state} done:{done}')
        #new_state = np.reshape(state, [1, self.state_size])
        # self.player_two.agent.save_model("success.model")

        # self.player_two.agent.save("drive/tictactoe/tictactoemodelnewfinal.h5")
        # self.player_two.agent.save_target("drive/tictactoe/tictactoetargetfinal.h5")
        print('Good Bye')
