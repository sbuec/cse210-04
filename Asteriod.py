import pyray as pr
from random import randint

class Asteriod:

    def __init__(self, window_width: int, window_height: int, texture: pr.Texture) -> None:
        self.win_width = window_width
        self.win_height = window_height
        self.texture = texture
        self.set_timer()

    def set_timer(self) -> None:
        self.timer = randint(0, 10)*60

    @staticmethod
    def create_image(character, font_size, color) -> pr.Image:
        return pr.image_text(character, font_size, color)

    @staticmethod
    def load_texture(character, font_size, color) -> pr.Texture:
        image = Asteriod.create_image(character, font_size, color)
        return pr.load_texture_from_image(image)
    
    @staticmethod
    def draw_rectangle(texture, pos_x, pos_y) -> None:
        pr.draw_texture_rec(
            texture,
            pr.Rectangle(0,0, float(texture.width), float(texture.height)),
            [pos_x, pos_y],
            pr.WHITE
        )
    
    @staticmethod
    def update_actor(actor) -> None:
        actor.pos_y += 1
    
    @classmethod
    def load_asteroid(cls, amount, win_width, win_height, texture) -> None:
        for _ in range(amount):
            cls(win_width, win_height, texture)
    
    @classmethod
    def draw_asteriod(cls) -> None:
        cls.timer_watch()
        for asteroid in cls.on_screen:
            if asteroid.pos_y >= asteroid.win_height - asteroid.texture.height:
                cls.on_screen.remove(asteroid)
                asteroid.set_timer()
            else:
                cls.update_actor(asteroid)
                asteroid.draw()
    
    @classmethod
    def timer_watch(cls) -> None:
        for asteroid in cls.all_created:

            if asteroid.timer <= 0 and asteroid not in cls.on_screen:
                asteroid.set_pos()
                cls.on_screen.append(asteroid)

            if asteroid.timer > 0 and asteroid in cls.on_screen:
                cls.on_screen.remove(asteroid)
            elif asteroid.timer > 0:
                asteroid.timer -= 1