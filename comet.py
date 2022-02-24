from Asteriod import Asteriod
from pyray import Texture

class Comet(Asteriod):
    '''
    A class of Asteroids, large clusters of rocks.
    '''

    _on_screen = []
    _all_created = []

    def __init__(self, window_width: int, window_height: int, texture: Texture) -> None:
        super().__init__(window_width, window_height, texture)
        self.points = -5
        Comet._on_screen.append(self)
        Comet._all_created.append(self)