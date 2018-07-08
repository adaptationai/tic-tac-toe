import json
import pickle
import random
from collections import deque
import os

import keras.backend as K
import numpy as np
from keras.layers import Dense, Dropout, Input, Activation
from keras.layers.merge import Add, Multiply
from keras.models import Model, Sequential, load_model, model_from_json
from keras.optimizers import Adam


class DQN:
    # def __init__(self, env):
    def __init__(self, env, state_size, action_size, epsilon, load):
        self.env = env
        

        self.gamma = 0.99
        self.epsilon = epsilon
        self.epsilon_min = 0.0
        self.epsilon_decay = 0.99999
        self.learning_rate = 0.00025
        self.tau = .125
        self.load = load
        self.model = self.create_model()
        self.target_model = self.create_model()
        self.memory = deque(maxlen=10000000)
        self.state_size = state_size
        self.action_size = action_size
        if self.load:
            #self.ensure_dir("tictactoe/data2")
            self.model = load_model("tictactoe/data/tictactoemodel2.h5")
            self.target_model = load_model(
                "tictactoe/data/tictactoetarget2.h5")
            #self.load_memory("tictactoe/data/ticdeque.pkl")

    def create_model(self):
        model = Sequential()
        #state_shape  = self.env.observation_space.shape
        #model.add(Dense(24, input_dim=state_shape[0], activation="relu"))
        model.add(Dense(24, input_dim=9, activation="relu"))
        model.add(Dense(48, activation="relu"))
        model.add(Dense(24, activation="relu"))
        # model.add(Dense(self.env.action_space.n))
        model.add(Dense(9))
        model.compile(loss="mean_squared_error",
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def act(self, state):
        self.epsilon *= self.epsilon_decay
        self.epsilon = max(self.epsilon_min, self.epsilon)
        if np.random.random() < self.epsilon:
            return random.randrange(self.action_size)
        # print(np.argmax(self.model.predict(state)[0]))
        # argsort = np.argsort(self.model.predict(state)[0])
        # predict = self.model.predict(state)[0]
        argmax = np.argmax(self.model.predict(state)[0])
        #print(f' argsort: {np.argsort(self.model.predict(state)[0])} predict: {self.model.predict(state)[0]} argmax: {np.argmax(self.model.predict(state)[0])} ')
        return argmax


    def remember(self, state, action, reward, new_state, done):
        self.memory.append([state, action, reward, new_state, done])

    def replay(self):
        batch_size = 32
        if len(self.memory) < batch_size:
            return
        
        samples = random.sample(self.memory, batch_size)
        for sample in samples:
            #if len(sample) == 5:
            state, action, reward, new_state, done = sample
            target = self.target_model.predict(state)
            if done:
                target[0][action] = reward
            else:
                Q_future = max(self.target_model.predict(new_state)[0])
                # print(Q_future)
                target[0][action] = reward + Q_future * self.gamma
            self.model.fit(state, target, epochs=1, verbose=0)
        return

    def target_train(self):
        weights = self.model.get_weights()
        target_weights = self.target_model.get_weights()
        for i in range(len(target_weights)):
            target_weights[i] = weights[i] * self.tau + \
                target_weights[i] * (1 - self.tau)
        self.target_model.set_weights(target_weights)

    def save_model(self, name):
        self.model.save(name)

    def save_model_weights(self, name):

        self.model.save_weights(name)

    def load_model(self, name):
        del self.model
        self.model = load_model(name)

    def load_model_weights(self, name):
        del self.model
        self.model = load_model(name)

    def save_target_weights(self, name):
        self.target_model.save_weights(name)

    def save_target(self, name):
        self.target_model.save(name)

    def load_target(self, name):
        del self.target_model
        self.target_model = load_model(name)
        # self.target_model.load_weights(name)

    def load_target_weights(self, name):

        self.target_model.load_weights(name)

    def save_memory(self, name):
        output = open(name, 'wb')
        pickle.dump(self.memory, output)
        output.close()

    def load_memory(self, name):

        pkl_file = open(name, 'rb')
        self.memory = pickle.load(pkl_file)
        pkl_file.close()

    def ensure_dir(self, file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
