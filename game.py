import random


'''This is a game that consists of a grid-like game board, which contains a monster and a door. The player is dropped into the game board, and must reach the door before being eaten by the monster in order to win.'''

CELLS = [(0,0), (0,1), (0,2),
        (1,0), (1,1), (1,2),
        (2,0), (2,1), (2,2)]

def get_locations():
    # need random locations for monster, door, and start
    # if monster, door, or start are the same, reset
    # return monster, door, and start locations

def move_player(player, move):
    # Get player's current location
    # if move is LEFT, y - 1
    # if move is RIGHT, y + 1
    # if move is UP, x - 1
    # if move is DOWN, x + 1
    # return player's new location

def get_moves(player):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    #if player's y is 0, remove ability to move left.
    # if player's x is 0, remove ability to move up.
    # if player's y is 2, remove ability to move right.
    # if player's x is 2, remove ability to move down.
    return MOVES


while True:
    print("Welcome to the Thunder Dungeon! You are now my prisoner. Escape... IF YOU DARE!")
    print("You are currently in room {}")
    print("You can move {}")
    print("Enter QUIT to exit the game.")

    move = raw_input("> ").upper()
    if move == "QUIT":
        print("I could tell you weren't cut out for my dungeon.")
        break
