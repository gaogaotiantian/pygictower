# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/gaogaotiantian/pygictower/blob/master/NOTICE

from .game_global import GameGlobal
from .game_character import Character


class Game:
    def __init__(self):
        self._maps = []
        self._curr_map_idx = 0
        self._global_state = GameGlobal()
        self.hero = Character()

    # ========================================================================
    # User Interface
    # ========================================================================
    def move(self, direction):
        pass

    @property
    def current_map(self):
        return None

    def get_floor(self, floor):
        pass

    # ========================================================================
    # Internal Methods
    # ========================================================================
    def _generate_maps(self):
        """
        generate the full maps
        overwrite self._maps
        """

    def _action(self, action_type, action_args):
        """
        This is the MUST path to communicate to Game object

        :param str action_type: action type indicator
        :param dict action_args: arguments for this action
        :return {"event": <str>, "event_args": <dict>}
        """
        pass

    def _action_move(self, direction):
        result = self.hero.move(self.current_map, direction)
        return result
