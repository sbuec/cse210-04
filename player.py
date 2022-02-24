from Asteriod import Actor

class Player(Actor):

    def __init__(self, window_width:int, window_height:int, texture) -> None:
        '''You need These 4 varibales in order to work with my classes'''
        self.win_width = window_width
        self.win_height = window_height
        self.texture = texture
        self.pos_x = self.win_width//2 - self.texture.width
        self.pos_y = self.win_height - self.texture.height
        self.points = 0
    
    def draw_player(self):
        self.draw_rectangle(self.texture, self.pos_x, self.pos_y)

    def update_position(self, pos_update):
        if 0 < self.pos_x + pos_update[0] < self.win_width - self.texture.width:
            self.pos_x += pos_update[0]

        if 0 < self.pos_y + pos_update[1] < self.win_height -  self.texture.height:
            self.pos_y += pos_update[1]