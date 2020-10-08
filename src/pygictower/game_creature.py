# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/gaogaotiantian/pygictower/blob/master/NOTICE

from .game_object import GameObject


class Creature(GameObject):
    def __init__(self, **kwargs):
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.gold = 0
        self.exp = 0
        self.floor = 0
        self.x = 0
        self.y = 0

        super().__init__(**kwargs)
