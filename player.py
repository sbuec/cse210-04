import pyray as pr

class Player:

    def __init__(self, window_width, window_height, texture: pr.Texture) -> None:
        '''You need These 4 variables in order to work with my classes'''
        self.win_width = window_width
        self.win_height = window_height
        self.texture = texture
        self.points = 0