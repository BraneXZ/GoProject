import argparse
import numpy as np

from dlgo.encoders import get_encoder_by_name
from dlgo import goboard_fast as goboard
from dlgo import mcts
from dlgo.utils import print_board, print_move

def generate_games(board_size, rounds, max_moves, temperature):
    boards, moves = [], [] #In boards you store encoded board state; moves is for encoded moves
    
    encoder = get_encoder_by_name('oneplane', board_size) #Initialize a OnePlaneEncoder by name with given board size
    
    game = goboard.GameState.new_game(board_size) #A new game of size board_size is instantiated
    
    bot = mcts.MCTSAgent(rounds, temperature)
    
    num_moves = 0
    while not game.is_over():
        print_board(game.board)
        move = bot.select_move(game)
        if move.is_play:
            boards.append(encoder.encode(game))
            
            move_one_hot = np.zeros(encoder.num_point())
            move_ont_hot[encoder.encode_point(move.point)] = 1
            moves.append(move_one_hot)
        
        print_move(game.next_player, move)
        game = game.apply_move(move)
        num_moves += 1
        if num_moves > max_moves:
            break
        
    return np.array(boards), np.array(moves)