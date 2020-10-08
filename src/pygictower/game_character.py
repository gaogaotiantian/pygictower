# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/gaogaotiantian/pygictower/blob/master/NOTICE

from .game_creature import Creature


class Character(Creature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def move(self, current_map, direction):
        pass

    def fight(self, monster):
        pass
