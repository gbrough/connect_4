#connect 4 game

import random
import sys

#board lay-out
board = [0]*42

#print the board
def print_board():
    print("")
    print("+" + "---+"*7)
    print("|" + "   |"*7)
    for i in range(0,42,7):
        print("|" + " " + str(board[i]) + " |" + " " + str(board[i+1]) + " |" + " " + str(board[i+2]) + " |" + " " + str(board[i+3]) + " |" + " " + str(board[i+4]) + " |" + " " + str(board[i+5]) + " |" + " " + str(board[i+6]) + " |")
        print("+" + "---+"*7)

#check if the game is over
def is_game_over():
    for i in range(0,42,7):
        if board[i] == board[i+1] == board[i+2] == board[i+3] == board[i+4] == board[i+5] == board[i+6] != 0:
            print("Game Over")
            sys.exit()
    for i in range(0,7):
        if board[i] == board[i+7] == board[i+14] == board[i+21] == board[i+28] == board[i+35] == board[i+42] != 0:
            print("Game Over")
            sys.exit()
    if board[0] == board[7] == board[14] == board[21] == board[28] == board[35] == board[42] != 0:
        print("Game Over")
        sys.exit()
    if board[1] == board[8] == board[15] == board[22] == board[29] == board[36] == board[43] != 0:
        print("Game Over")
        sys.exit()
    if board[2] == board[9] == board[16] == board[23] == board[30] == board[37] == board[44] != 0:
        print("Game Over")
        sys.exit()
    if board[3] == board[10] == board[17] == board[24] == board[31] == board[38] == board[45] != 0:
        print("Game Over")
        sys.exit()
    if board[4] == board[11] == board[18] == board[25] == board[32] == board[39] == board[46] != 0:
        print("Game Over")
        sys.exit()
    if board[5] == board[12] == board[19] == board[26] == board[33] == board[40] == board[47] != 0:
        print("Game Over")
        sys.exit()
    if board[6] == board[13] == board[20] == board[27] == board[34] == board[41] == board[48] != 0:
        print("Game Over")
        sys.exit()

#check if the move is valid
def is_valid_move(move):
    if move < 0 or move > 49:
        return False
    if board[move] != 0:
        return False
    return True

#make a move
def make_move(move, player):
    if player == 1:
        board[move] = 'X'
    else:
        board[move] = 'O'

#check if the move is valid for AI
def is_valid_move_for_ai(move):
    if move < 0 or move > 49:
        return False
    if board[move] != 0:
        return False
    return True

#make a move for AI
def make_move_for_ai(move):
    if board[move] != 0:
        return False
    board[move] = 'O'
    return True

def is_valid_move_for_ai_2(move):
    if move < 0 or move > 49:
        return False
    if board[move] != 0:
        return False
    return True

def __init__():
    print("Welcome to Connect 4")
    print("")
    print("Player 1 is X")
    print("Player 2 is O")
    print("")
    print("To make a move, enter the column number")
    print("")
    print_board()
    
def play_game():
    player = 1
    while True:
        if player == 1:
            move = int(input("Player 1: "))
            if is_valid_move(move):
                make_move(move, player)
                print_board()
                player = 2
            else:
                print("Invalid Move")
                print_board()
        else:
            move = int(input("Player 2: "))
            if is_valid_move(move):
                make_move(move, player)
                print_board()
                player = 1
            else:
                print("Invalid Move")
                print_board()
        is_game_over()

play_game()


