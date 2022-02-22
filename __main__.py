import pyray as pr
import rock as Rk
import utils
import services.keyboard_service
import services.video_service
#import input



'''
Variables that will be used throughout the program
'''
HEIGHT = 450
WIDTH = 800
FPS = 60
CAPTION = "Hello Pyray"


def main():

    '''
    Creating objects and settings that will be used 
    '''
    pr.init_window(WIDTH, HEIGHT, CAPTION)
    pr.set_target_fps(FPS)

    rock_texture = Rk.Rock.load_texture('O', 12, pr.WHITE)
    Rk.Rock.load_asteroid(200, WIDTH, HEIGHT, rock_texture)

    #creating instance of keyboard service
    ks = services.keyboard_service.KeyboardService()

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
        Rk.Rock.draw_asteriod()
        
        #checking for input
        #currently an example to show that input_direction is working
        direction = ks.input_direction()
        if direction == 1:
            pr.draw_text("Working", 50, 50, 20, pr.WHITE)




        pr.end_drawing()





    pr.close_window()

if __name__ == "__main__":
    main()
