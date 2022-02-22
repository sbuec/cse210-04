from Asteriod import Asteriod
from pyray import Texture

class Gem(Asteriod):
    '''
    A class of Asteroids
    '''

    _on_screen = []
    _all_created = []

    def __init__(self, window_width: int, window_height: int, texture: Texture) -> None:
        super().__init__(window_width, window_height, texture)
        self.points = 2
        Gem._on_screen.append(self)
        Gem._all_created.append(self)