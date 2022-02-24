import numpy
from Asteriod import Actor

class Player(Actor):

    def __init__(self, window_width:int, window_height:int, texture) -> None:
        '''You need These 4 varibales in order to work with my classes'''
        self.win_width = window_width
        self.win_height = window_height
        self.pos_x = self.win_width//2
        self.pos_y = self.win_height-10
        self.texture = texture
        self.points = 0
    
    def draw_player(self):
        self.draw_rectangle(self.texture, self.pos_x, self.pos_y)

    def update_position(self, pos_update):
        self.pos_x += pos_update[0]
        self.pos_y += pos_update[1]
        self.pos_y = numpy.clip(self.pos_y, 360, 440)