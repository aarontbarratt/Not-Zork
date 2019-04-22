from enum import Enum
from player import Player


class GameState(Enum):
    on = 1
    off = 0


class Command(Enum):
    look = 0
    walk = 1


player_name = input()
player = Player(player_name.lower)
game_state = GameState.on


def inputs(prompt):
    print('input')
    if prompt == Command.look.name:
        pass
    else:
        print(' is confused and doesn\'t know what do')


def main_loop():
    while game_state == GameState.on:
        player_input = input()
        inputs(player_input)


main_loop()

