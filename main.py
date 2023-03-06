#from lib import sokoban
import pygame
from lib.sokoban import sokoban

game = sokoban()
game.init()

try:

    running = True
    while running:
        game.update_dsp()
        for event in game.events:
            if event.type == pygame.QUIT:
                print("\n\nPyGame quit event detected. Exiting...\n")
                running = False

    try:
        game.quit()
        print("Exit Success!\n")
    except Exception as e:
        print("Exit Failure!\n")
        raise e
    
except KeyboardInterrupt:
    
    print("\n\nKeyboard interrupt detected. Exiting...\n")
    try:
        game.quit()
        print("Exit Success!\n")
    except Exception as e:
        print("Exit Failure!\n")
        raise e

