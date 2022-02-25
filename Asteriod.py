import random
import pyray as pr
from random import randint

class Actor:
    '''
    Holds methods for creating images, loading textures, and drawing rectangles
    '''

    @staticmethod
    def create_image(character:str , font_size:int , color: pr.Vector4) -> pr.Image:
        '''
        Creates image from text
        
        Returns:
        - pr.Image
        '''
        return pr.image_text(character, font_size, color)

    @staticmethod
    def load_texture(character, font_size, color = 0) -> pr.Texture:
        '''
        Takes a string and makes it a pr.Texture

        Returns:
        - pr.Texture
        '''
        image = Asteriod.create_image(character, font_size, color)
        return pr.load_texture_from_image(image)
    
    @staticmethod
    def draw_rectangle(texture, pos_x, pos_y) -> None:
        '''
        Creates a rectangle, renders it's texture, and places it on screen
        '''
        pr.draw_texture_rec(
            texture,
            pr.Rectangle(0,0, float(texture.width), float(texture.height)),
            [pos_x, pos_y],
            pr.WHITE
        )

class Asteriod(Actor):
    '''
    Base class for Gem and Rock classes
    '''

    def __init__(self, window_width: int, window_height: int, texture: pr.Texture) -> None:
        self.win_width = window_width
        self.win_height = window_height
        self.texture = texture
        self.set_pos()
        self.set_timer()

    def draw(self) -> None:
        '''
        Renders rectangle with a texture in a position(x,y) on the screen
        '''
        self.draw_rectangle(self.texture, self.pos_x, self.pos_y)

    def set_timer(self) -> None:
        '''
        Timer for when the Asteroids appear on the screen
        '''
        self.timer = randint(0, 10)*60

    def set_pos(self) -> None:
        '''
        Randomly sets the position of Asteroids at the top of the screen
        '''
        self.pos_x = randint(0, self.win_width - self.texture.width)
        self.pos_y = 0
    
    @staticmethod
    def update_actor(actor) -> None:
        '''
        Moves Asteroids down the screen
        '''
        actor.pos_y += 1
    
    @staticmethod
    def check_collision(asteroid, player ) -> bool:
        '''
        Checks for a collision between an Asteroid and the Player

        Returns:
        - boolean
        '''
        return pr.check_collision_recs(
                [asteroid.pos_x, asteroid.pos_y,asteroid.texture.width, asteroid.texture.height],
                [player.pos_x, player.pos_y, player.texture.width, player.texture.height]
            )
    
    @classmethod
    def load_asteroid(cls, amount: int, win_width: int, win_height: int, texture: pr.Texture) -> None:
        '''
        Loads 'amount' of Asteroids on screen
        '''
        for _ in range(amount):
            cls(win_width, win_height, texture)
    
    @classmethod
    def draw_asteroid(cls, player) -> None:
        '''
        Main draw function for a single Class of Asteroids
        '''
        cls.timer_watch()
        for asteroid in cls._on_screen:
            cls.collisions_watch(asteroid, player)
            if asteroid.pos_y >= asteroid.win_height - asteroid.texture.height:
                cls._on_screen.remove(asteroid)
                asteroid.set_timer()
            else:
                cls.update_actor(asteroid)
                asteroid.draw()
    
    @classmethod
    def timer_watch(cls) -> None:
        '''
        Updates and manages the Asteroid timer variable and anything associated with it
        '''
        for asteroid in cls._all_created:

            if asteroid.timer <= 0 and asteroid not in cls._on_screen:
                asteroid.set_pos()
                cls._on_screen.append(asteroid)

            if asteroid.timer > 0 and asteroid in cls._on_screen:
                cls._on_screen.remove(asteroid)
            elif asteroid.timer > 0:
                asteroid.timer -= 1
    
    @classmethod
    def collisions_watch(cls, asteroid, player) -> None:
        '''
        Watches for and manages the collisions between Asteroids and the Player
        '''
        if cls.check_collision(asteroid, player):
            cls._on_screen.remove(asteroid)
            asteroid.pos_y = 0
            player.points += asteroid.points
            # 0 point minimum
            if(player.points <= 0):
                player.points = 0
