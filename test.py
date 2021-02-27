import chess.pgn 
import chess
import requests
import os 
import numpy as np 

# np.set_printoptions(threshold=np.inf)

# print(np.load('/Users/rogermcgrath/Desktop/dlchess/data/training/Hikaru_0220train_features_1.npy'))
counter = 0
for subdir, dirs, files in os.walk('/Users/rogermcgrath/Desktop/dlchess/data/training'):
    for file in files:
        if file[-4:] == '.npy' or file[-6] == 'icloud' or file[0] == '.':
            os.remove('/Users/rogermcgrath/Desktop/dlchess/data/training/' + file)
        counter += 1
print(counter)

# pgn = open('/Users/rogermcgrath/Desktop/dlchess/data/test/Viswanathan_Anand.pgn')
# coutner = 14
# while True:
#     headers = chess.pgn.read_headers(pgn)
#     print(headers)
#     if headers is None:
#         break
                   
#     file = open('/Users/rogermcgrath/Desktop/dlchess/data/test/Viswanathan_Anad_' + str(coutner) + '.pgn', 'w')
#     file.write(str(chess.pgn.read_game(pgn)))
#     coutner += 1
# print(coutner)


# link = 'https://api.chess.com/pub/player/Hikaru/games/2021/02/pgn'
# response = requests.get(link)

# pgn = open('/Users/rogermcgrath/Desktop/dlchess/Hikaru.pgn', 'w')
# pgn.write(response.text)

# pgn = open('/Users/rogermcgrath/Desktop/dlchess/Hikaru.pgn')
# games = chess.pgn.read_game(pgn)
# coutner = 0

# while True:
#     headers = chess.pgn.read_headers(pgn)
#     if headers is None:
#         break
#     else:
#         file = open('/Users/rogermcgrath/Desktop/dlchess/Hikaru' + str(coutner) + '.pgn', 'w')
#         file.write(str(chess.pgn.read_game(pgn)))
#         coutner += 1
    
# os.remove('/Users/rogermcgrath/Desktop/dlchess/Hikaru' + str(coutner - 1) + '.pgn')
    
    