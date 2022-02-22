import pyray

class KeyboardService:

    def __init__(self, cell_size = 1):
        self._cell_size = cell_size


    def input_direction(self):
        if pyray.is_key_down(pyray.KEY_LEFT):
            return -1

        if pyray.is_key_down(pyray.KEY_RIGHT):
            return 1

        if pyray.is_key_down(pyray.KEY_UP):
            return -1

        if pyray.is_key_down(pyray.KEY_DOWN):
            return 1
