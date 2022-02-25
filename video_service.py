import pyray as pr
import gem as gm
import rock as rk
import player as pl
import comet as cm
import keyboard_service as ks


'''
For setup and running the display
'''
class Game:
    def __init__(self,  width, height, caption, fps, gem_amount, rock_amount, comet_amount):
        self.width = width
        self.height = height
        self.caption = caption
        self.fps = fps
        self.gem_amout = gem_amount
        self.rock_amount = rock_amount
        self.comet_amount = comet_amount

    def run(self):
        '''
        Creating objects and settings that will be used 
        '''
        pr.init_window(self.width, self.height, self.caption)
        pr.set_target_fps(self.fps)

        # Loads player
        player_texture = pl.Player.load_texture('#', 16 ,pr.WHITE)
        player = pl.Player(self.width, self.height, player_texture)

        # Loads rocks
        rock_texture = rk.Rock.load_texture('O', 16, pr.WHITE)
        rk.Rock.load_asteroid(self.rock_amount, self.width, self.height, rock_texture)

        # Loads Gems
        gem_texture = gm.Gem.load_texture('*', 16, pr.GREEN)
        gm.Gem.load_asteroid(self.gem_amout, self.width, self.height, gem_texture)

        #Loads Asteroids
        comet_texture = cm.Comet.load_texture('[X]', 16, pr.YELLOW)
        cm.Comet.load_asteroid(self.comet_amount, self.width, self.height, comet_texture)

        while not pr.window_should_close():
            '''
            Things to do while window is open and game is running
            *Display output
            *Receive input
            *Calculate automatic changes to the output
            '''

            pr.begin_drawing()
            pr.clear_background(pr.BLACK)

            #Keyboard update
            pos_update = ks.KeyboardService.input_direction()
            player.update_position(pos_update)
            player.draw_player()

            #Displays points
            pr.draw_text(f"Points {player.points}", 20, 20, 20, pr.YELLOW)

            # The three lines below are the reason for the 4 variables needed in the player class
            rk.Rock.draw_asteroid(player)
            gm.Gem.draw_asteroid(player)
            cm.Comet.draw_asteroid(player)

            #currently an example to show that input_direction is working
            pr.end_drawing()

        pr.close_window()
