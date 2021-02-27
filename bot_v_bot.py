import chess
import sys 
sys.path.append('/Users/rogermcgrath/Desktop/dlchess/agent')
sys.path.append('/Users/rogermcgrath/Desktop/dlchess/encoders')
sys.path.append('/Users/rogermcgrath/Desktop/dlchess/data')
from oneplane import OnePlaneEncoder
# from predict import DeepLearningAgent, load_prediction_agent
from processor import ChessDataProcessor
from layers import layers
import h5py
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.callbacks import ModelCheckpoint

np.set_printoptions(threshold=np.inf)

to_squares, from_squares = 8,8
num_classes = 64*64
num_games = 100

encoder = OnePlaneEncoder((to_squares, from_squares))

processor = ChessDataProcessor(data_directory='/Users/rogermcgrath/Desktop/dlchess/data/training')


# generator = processor.load_chess_data('train', num_games, use_generator=True)
# test_generator = processor.load_chess_data('test', num_games, use_generator=True)
input_shape = (encoder.num_planes, to_squares, from_squares)
X, y = processor.load_chess_data(num_samples=100)
model = Sequential()
network_layers = layers(input_shape)
for layer in network_layers:
    model.add(layer)
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])

model.fit(X, y, batch_size=128, epochs=5, verbose=1)

model.save("chess_bot_v0.1")