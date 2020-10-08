# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/gaogaotiantian/pygictower/blob/master/NOTICE

import random
import time


class GameGlobal:
    def __init__(self, seed=int(time.time())):
        self._seed = seed
        self._state = random.getstate()
        random.seed(seed)

    def random(self):
        return random.random()

    def randrange(self, a, b):
        return a + int((b - a) * self.random())

    def store_random_state(self):
        self._state = random.getstate()

    def load_random_state(self):
        random.setstate(self._state)
