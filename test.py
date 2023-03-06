from lib.sokoban import sokoban
import pygame
import numpy as np
import matplotlib.pyplot as plt



'''
im = plt.imread("lib/bin/s.png")
plt.imshow(im)
plt.xlim((195,249))
plt.ylim((301,247))
plt.show()
'''

wall = plt.imread("lib/bin/wall.png")
plt.imshow(wall)
plt.show()

pygame.init()
rect = pygame.Rect(10,20,30,30)
#dsp = pygame.display.set_mode((800,800))

fuck=1
while fuck:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            fuck=0
    pygame.display.flip()
    