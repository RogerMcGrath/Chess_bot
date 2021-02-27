import chess.pgn
import requests
import os

def get_games(data_directory, gamers, months, year):
    for gamer in gamers:
        for month in months:
            link = 'https://api.chess.com/pub/player/' + gamer + '/' + 'games' + '/' + year + '/' + month + '/' + 'pgn'
            pgns = requests.get(link)
            print(data_directory + '/' + gamer + '_' + month + '.pgn')
            write = open(data_directory + '/' + gamer + '_' + month + '.pgn', 'w')
            write.write(pgns.text)
            pgn = open(data_directory + '/' + gamer + '_' + month + '.pgn')
            coutner = 0
            while True:
                headers = chess.pgn.read_headers(pgn)
                if headers is None:
                    break
                   
                file = open(data_directory + '/' + gamer + '_' + month + str(coutner) + '.pgn', 'w')
                file.write(str(chess.pgn.read_game(pgn)))
                coutner += 1
            os.remove(data_directory + '/' + gamer + '_' + month + '.pgn')

get_games('/Users/rogermcgrath/Desktop/dlchess/data/training', ['FabianoCaruana', 'DanielNaroditsky', 'Jospem', 'exoticprincess','Hikaru','AlexandraBotez','GothamChess'], ['01','02'], '2019')
