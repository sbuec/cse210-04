import pyray

class KeyboardService:

    def input_direction():
        if pyray.is_key_down(pyray.KEY_LEFT):
            return -2

        if pyray.is_key_down(pyray.KEY_RIGHT):
            return 2