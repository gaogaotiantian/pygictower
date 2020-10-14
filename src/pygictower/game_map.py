# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/gaogaotiantian/pygictower/blob/master/NOTICE

from game_cell import Cell
from game_global import GameGlobal
import random


ROOM_PROB = 0.1

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
        for i in range(self.size):
            self._cells.append([])
            for j in range(self.size):
                self._cells[i].append(Cell(self._global_state))

        wall_list = set()
        n_rooms = 0
        start = (self._global_state.randrange(0, self.size), self._global_state.randrange(0, self.size))
        # print(start)
        self._cells[start[0]][start[1]].walkable = True
        wall_list.update(self.get_surrounding(start[0], start[1]))
        while wall_list:
            wall = random.choice(list(wall_list))
            # print(wall)
            virtical = self._global_state.random() > 0.5
            v = self._other_cell((wall[0] - 1, wall[1]), (wall[0] + 1, wall[1]))
            h = self._other_cell((wall[0], wall[1] + 1), (wall[0], wall[1] - 1))
            if virtical:
                cell = v if v else h
            else:
                cell = h if h else v
            if cell == (-1, -1):
                self._cells[wall[0]][wall[1]].walkable = True
            elif cell:
                if self._global_state.random() <= ROOM_PROB and n_rooms < self.size/5:
                    center = self.cell_add(cell, self.cell_diff(cell, wall))
                    valid, outer = self.check_valid_room(center)
                    if not self._is_valid(center) or not valid:
                        wall_list.update(self.get_surrounding_walls(cell[0], cell[1]))
                    else:
                        # print("room at {}".format(center))
                        surr = self.get_surrounding_8(center[0], center[1])
                        for c in surr:
                            if c in wall_list:
                                wall_list.remove(c)
                            else:
                                self._cells[c[0]][c[1]].walkable = True
                        self._cells[center[0]][center[1]].walkable = True
                        for c in outer:
                            if c in wall_list:
                                wall_list.remove(c)
                        n_rooms += 1
                else:
                    wall_list.update(self.get_surrounding_walls(cell[0], cell[1]))

                self._cells[wall[0]][wall[1]].walkable = True
                self._cells[cell[0]][cell[1]].walkable = True
            if wall in wall_list:
                wall_list.remove(wall)

    def _other_cell(self, cell1, cell2):
        if not self._is_valid(cell1):
            if self._cells[cell2[0]][cell2[1]].walkable:
                return (-1, -1)
            else:
                return None

        if not self._is_valid(cell2):
            if self._cells[cell1[0]][cell1[1]].walkable:
                return (-1, -1)
            else:
                return None

        if (self._cells[cell1[0]][cell1[1]].walkable) and not (self._cells[cell2[0]][cell2[1]].walkable):
            return cell2
        if not (self._cells[cell1[0]][cell1[1]].walkable) and (self._cells[cell2[0]][cell2[1]].walkable):
            return cell1

        return None

    def _is_valid(self, c):
        return 0 <= c[0] < self.size and 0 <= c[1] < self.size

    def get_surrounding(self, x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = []
        for d in directions:
            if self._is_valid((x + d[0], y + d[1])):
                res.append((x + d[0], y + d[1]))
        return res
    
    def get_surrounding_walls(self, x, y):
        res = set()
        for i, j in self.get_surrounding(x, y):
            if not self._cells[i][j].walkable:
                res.add((i, j))
        return res

    def get_surrounding_8(self, x, y):
        directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        res = set()
        for d in directions:
            if self._is_valid((x + d[0], y + d[1])):
                res.add((x + d[0], y + d[1]))
        res.update(self.get_surrounding(x, y))
        return res

    def cell_diff(self, c1, c2):
        return (c1[0] - c2[0], c1[1] - c2[1])
    
    def cell_add(self, c, add):
        return (c[0] + add[0], c[1] + add[1])

    def check_valid_room(self, center):
        if not self._is_valid(center):
            return False, set()
        surr = self.get_surrounding_8(center[0], center[1])
        surr.add(center)
        outer = set()
        for c in surr:
            if self._cells[c[0]][c[1]].walkable:
                return False, set()
            surr2 = self.get_surrounding_8(c[0],c[1])
            outer.update(surr2)
            for c2 in surr2:
                if self._cells[c2[0]][c2[1]].walkable:
                    return False, set()
        outer.difference_update(surr)
        return True, outer




if __name__ == "__main__":
    global_state = GameGlobal()
    map = GameMap(global_state, 15)
    map._generate_map()
    walkable = [[1 if c.walkable else 0 for c in map._cells[i]] for i in range(map.size)]
    for i in range(map.size):
        print(walkable[i])
