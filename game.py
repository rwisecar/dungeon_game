from __future__ import print_function
import random


'''This is a game that consists of a grid-like game board, which contains a monster and a door. The player is dropped into the game board, and must reach the door before being eaten by the monster in order to win.'''

CELLS = [(0,0), (0,1), (0,2),
        (1,0), (1,1), (1,2),
        (2,0), (2,1), (2,2)]

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    player = random.choice(CELLS)

    if monster == door or monster == player or door == player:
        return get_locations()

    return monster, door, player

def move_player(player, move):
    x, y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x -= 1

    return x, y

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')
    return moves

def draw_map(player):
    print(' _ _ _')
    tile = '|{}'

    for idx, cell in enumerate(CELLS):
        if idx in [0, 1, 3, 4, 6, 7]:
            if cell == player:
                print(tile.format('X'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))

def play_game():
    monster, door, player = get_locations()
    print("Welcome to the Thunder Dungeon! You are now my prisoner. Escape... IF YOU DARE!")

    while True:
        moves = get_moves(player)
        print("You are currently in room {}".format(player))
        draw_map(player)
        print("You can move {}".format(moves))
        print("Enter QUIT to exit the game.")

        move = raw_input("> ").upper()
        if move == "QUIT":
            print("I could tell you weren't cut out for my dungeon.")
            break

        if move in moves:
            player = move_player(player, move)
            continue
        else:
            print("** Walls are hard, stop walking into them! **")
            continue

        if player == door:
            print("You escaped!")
            break
        elif player == monster:
            print("You were eaten by the monster!")
            break


play_game()
