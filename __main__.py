import pyray as pr
import gem as gm
import player as pl
import utils
import input

def main():
    HEIGHT = 450
    WIDTH = 800

    GEM_AMOUNT = 20
    ROCK_AMOUNT = 150

    pr.init_window(WIDTH, HEIGHT, "Hello Pyray")
    pr.set_target_fps(60)

    rock_texture = rk.Rock.load_texture('O', 12, pr.WHITE)
    rk.Rock.load_asteroid(ROCK_AMOUNT, WIDTH, HEIGHT, rock_texture)

    gem_texture = gm.Gem.load_texture('*', 12, pr.GREEN)
    gm.Gem.load_asteroid(GEM_AMOUNT, WIDTH, HEIGHT, gem_texture)


    while not pr.window_should_close():

        pr.begin_drawing()

        pr.clear_background(pr.BLACK)

        # The two lines below are the reason for the 4 variables needed in the player class
        rk.Rock.draw_asteroid(player)
        gm.Gem.draw_asteroid(player)

        pr.end_drawing()

    pr.close_window()

if __name__ == "__main__":
    main()