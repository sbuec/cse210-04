import video_service as vs


'''
Variables that will be used throughout the program
'''
HEIGHT = 450
WIDTH = 800
FPS = 60
CAPTION = "Greed"

GEM_AMOUNT = 25
ROCK_AMOUNT = 150
COMET_AMOUNT = 8

def main():
    greed = vs.Game(WIDTH, HEIGHT, CAPTION, FPS, GEM_AMOUNT, ROCK_AMOUNT, COMET_AMOUNT)
    greed.run()

if __name__ == "__main__":
    main()