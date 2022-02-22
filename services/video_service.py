import pyray as pr


class Game:
    def __init__(self,  width, height, caption):
        pr.init_window(width, height, caption)
        pr.set_target_fps(60)

    def run(self):



        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(pr.RAYWHITE)
            pr.draw_text('Working', 200, 200, 20, pr.LIGHTGRAY)
            pr.end_drawing()

        pr.close_window()
