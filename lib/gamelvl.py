import numpy as np
import pygame
import lib.gameobj as gobj
from matplotlib.pyplot import imread,imshow,show

class maptile:
    
    def __init__(self, type: str, occ=None):
        self.type       = type
        self.iswall     = ("W" in self.type)
        self.isgoal     = ("G" in self.type)
        self.occupant   = occ

class gamelvl:

    def __init__(self,fname=None):
        self.title      = None
        self.textmap    = None
        self.shape      = tuple()
        self.static_map = None
        if fname is not None:
            self.loadmap(fname)

    def loadmap(self,filename):
        self.textmap = np.loadtxt(filename)
        self.title = filename[0:-4]
        self.shape = self.textmap.shape
        self.static_map = np.empty(self.shape)
        for r in range(self.textmap.shape[0]):
            for c in range(self.textmap.shape[1]):
                tp = self.textmap[r,c]
                if "P" in tp:
                    tp = "F"
                    occupant = gobj.player((r,c))
                elif "B" in tp:
                    tp = "F"
                    occupant = gobj.block((r,c))
                else:
                    occupant = None
                self.static_map[r,c] = maptile(tp,occupant)