from random import randint
from Asteriod import Asteriod
from pyray import Texture

class Rock(Asteriod):

    on_screen = []
    all_created = []

    def __init__(self, window_width: int, window_height: int, texture: Texture) -> None:
        super().__init__(window_width, window_height, texture)
        self.points = -1
        self.set_pos()
        Rock.on_screen.append(self)
        Rock.all_created.append(self)

    def draw(self) -> None:
        self.draw_rectangle(self.texture, self.pos_x, self.pos_y)

    def set_pos(self) -> None:
        self.pos_x = randint(0, self.win_width - self.texture.width)
        self.pos_y = 0