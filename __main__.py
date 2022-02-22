import pyray as pr
import gem as gm
import rock as rk
import player as pl
import utils
import services as Sv
#import input



'''
Variables that will be used throughout the program
'''
HEIGHT = 450
WIDTH = 800
FPS = 60
CAPTION = "Hello Pyray"

GEM_AMOUNT = 20
ROCK_AMOUNT = 150

def main():
    '''
    Creating objects and settings that will be used 
    '''
    pr.init_window(WIDTH, HEIGHT, CAPTION)
    pr.set_target_fps(FPS)

    # Loads rocks
    rock_texture = rk.Rock.load_texture('O', 12, pr.WHITE)
    rk.Rock.load_asteroid(ROCK_AMOUNT, WIDTH, HEIGHT, rock_texture)

     # Loads Gems
    gem_texture = gm.Gem.load_texture('*', 12, pr.GREEN)
    gm.Gem.load_asteroid(GEM_AMOUNT, WIDTH, HEIGHT, gem_texture)

    #creating instance of keyboard service
    ks = Sv.KeyboardService()

    while not pr.window_should_close():
        '''
        Things to do while window is open and game is running
        *Display output
        *Receive input
        *Calculate automatic changes to the output
        '''
        
        #Printing output
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        # The two lines below are the reason for the 4 variables needed in the player class
        rk.Rock.draw_asteroid(player)
        gm.Gem.draw_asteroid(player)

        #checking for input
        #currently an example to show that input_direction is working
        direction = ks.input_direction()
        if direction == 1:
            pr.draw_text("Working", 50, 50, 20, pr.WHITE)

        pr.end_drawing()

    pr.close_window()

if __name__ == "__main__":
    main()