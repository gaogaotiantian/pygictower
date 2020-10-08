# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/gaogaotiantian/pygictower/blob/master/NOTICE

from .game_engine import Game


class PygicTower:
    def __init__(self):
        pass

    def create_game(self):
        """
            return a Game object
        """
        self.game = Game()

        return self.game
