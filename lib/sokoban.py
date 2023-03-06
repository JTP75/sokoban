import numpy as np
import pygame
from lib.gamelvl import gamelvl
from lib.gameobj import player,block

class sokoban:

    def __init__(self):
        
        self.surface = None
        self.background_color = tuple()
        self.winres = tuple()

    def init(self,winres=(800,800),bclr=(32,32,64)):

        self.winres = winres
        self.background_color = bclr

        pygame.init()
        self.surface = pygame.display.set_mode(winres)
        pygame.display.set_caption("Sokoban")
        self.surface.fill(self.background_color)

    @property
    def events(self):

        return pygame.event.get()

    def quit(self):

        pygame.quit()

    def update_dsp(self):
        pass