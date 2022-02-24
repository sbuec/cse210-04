import pyray

class KeyboardService:

    @staticmethod
    def input_direction():
        update_pos = [0, 0]

        # X input
        if pyray.is_key_down(pyray.KEY_LEFT):
            update_pos[0] = -1.5
        if pyray.is_key_down(pyray.KEY_RIGHT):
            update_pos[0] = 1.5
        if pyray.is_key_down(pyray.KEY_D):
            update_pos[0] = 1.5
        if pyray.is_key_down(pyray.KEY_A):
            update_pos[0] = -1.5
        # Y input
        if pyray.is_key_down(pyray.KEY_UP):
            update_pos[1] = -1.5
        if pyray.is_key_down(pyray.KEY_DOWN):
            update_pos[1] = 1.5
        if pyray.is_key_down(pyray.KEY_W):
            update_pos[1] = -1.5
        if pyray.is_key_down(pyray.KEY_S):
            update_pos[1] = 1.5

        return update_pos