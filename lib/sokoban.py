import numpy as np
import pygame
from lib.gamelvl import gamelvl
from lib.gameobj import player,block

class sokoban:

    def __init__(self):
        self.screen             = None
        self.winres             = tuple()
        self.lvl                = None

    def init(self,winres=(800,800)):
        self.winres = winres
        pygame.init()
        pygame.display.set_icon(pygame.image.load("lib/bin/guy.png"))
        pygame.display.set_caption("Sokoban")
        self.screen = pygame.display.set_mode(winres)

    @property
    def events(self):
        return pygame.event.get()

    def quit(self):
        pygame.quit()

    def parse_events(self):
        for event in self.events:
            pass