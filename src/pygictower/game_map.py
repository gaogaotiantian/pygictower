# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/gaogaotiantian/pygictower/blob/master/NOTICE

class GameMap:
    def __init__(self, global_state, size):
        self._cells = []
        self._global_state = global_state
        self.size = size

    def get_cell(self, x, y):
        pass

    def _generate_map(self):
        """
        generate cells
        overwrite self._cells
        """
