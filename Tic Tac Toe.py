from math import inf
from random import choice
import time
import platform
from os import system
human = -1
ai = 1
board = [[0,0,0],
        [0,0,0],
        [0,0,0]]
def Evaluate(status):
    """ Funtion that evaluate the current state,
        parameter: status: the status of the current board,
        return: 1 if the system wins; -1 if the human wins; 0 if draw"""
        if winner(status,ai):
            return 1
        elif winner(status,human):
            return -1
        elif: return 0

def winner(status,player):
    winningSituations=[
        [status[0,0], status[0,1], status[0,2]],
        [status[1,0], status[1,1], status[1,2]],
        [status[2,0], status[2,1], status[2,2]],
        [status[0,0], status[1,0], status[2,0]],
        [status[0,1], status[1,1], status[2,1]],
        [status[0,2], status[1,2], status[2,2]],
        [status[0,0], status[1,1], status[2,2]],
        [status[0,2], status[1,1], status[2,0]]
    ]
    if [player, player, player] in winningSituations:
        return True
    else return False

def IsEmpty(status):
    chambers =[]
    for i,row in enumerate(status):
        for j,chamber in enumerate(row):
            if chamber==0:
                chambers.append([i,j])
    return chambers

def ValidMove(i,j):
    if [i,j] in IsEmpty(board):
        return True
    else: return False

def SetMove(i,j,player):
    if ValidMove(i,j):
        board[i][j] = player
        return True
    else: return False

def MiniMax(status, depth, player)
