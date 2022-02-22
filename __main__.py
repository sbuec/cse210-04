import pyray as pr
import rock as Rk
import utils
import input


def main():
    HEIGHT = 450
    WIDTH = 800

    pr.init_window(WIDTH, HEIGHT, "Hello Pyray")
    pr.set_target_fps(60)

    rock_texture = Rk.Rock.load_texture('O', 12, pr.WHITE)
    Rk.Rock.load_asteroid(200, WIDTH, HEIGHT, rock_texture)


    while not pr.window_should_close():

        pr.begin_drawing()

        pr.clear_background(pr.BLACK)

        Rk.Rock.draw_asteriod()

        pr.end_drawing()

    pr.close_window()

if __name__ == "__main__":
    main()
