import pygame
from lib.sokoban import sokoban

game = sokoban()
game.init()

try:

    running = True
    while running:
        game.screen.fill((0,0,255))
        game.parse_events()

    try:
        game.quit()
        print("Exit Success!\n")
    except Exception as e:
        print("Exit Failure!\n")
        raise e
    
except KeyboardInterrupt:
    print("\nKeyboard interrupt detected. Exiting...")
    try:
        game.quit()
        print("Exit Success!\n")
    except Exception as e:
        print("Exit Failure!\n")
        raise e

