import numpy as np
import pygame
import lib.gameobj as gobj
from matplotlib.pyplot import imread,imshow,show

class gametile:
    
    def __init__(self, type: str, occupant: None or gobj.block or gobj.player = None):
        self.type       = type
        self.iswall     = ("W" in self.type)
        self.isgoal     = ("G" in self.type)
        self.occupant   = occupant
        self.img        = np.empty((54,54))
        if self.iswall:
            self.img = imread("bin/wall.png")
        elif self.isgoal:
            self.img = imread("bin/goal.png")
        else:
            self.img = imread("bin/floor.png")

class gamelvl:

    def __init__(self,fname=None):
        self.FWBPG_map  = None
        self.shape      = tuple()
        self.tilemat    = None
        if fname is not None:
            self.loadmap(fname)

    def loadmap(self,filename):
        self.FWBPG_map = np.loadtxt(filename)
        self.shape = self.FWBPG_map.shape
        self.tilemat = np.empty(self.shape)
        for r in range(self.FWBPG_map.shape[0]):
            for c in range(self.FWBPG_map.shape[1]):
                tp = self.FWBPG_map[r,c]
                if tp=="P":
                    occupant = gobj.player((r,c))
                    tp = "F"
                elif tp=="B":
                    occupant = gobj.block((r,c))
                    tp = "F"
                else:
                    occupant = None
                self.tilemat[r,c] = gametile(tp,occupant)

    def reset(self):
        pass