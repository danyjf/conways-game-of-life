import pygame
from const import *

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = False
        
    def draw(self):
        rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)
        if not self.is_alive:
            pygame.draw.rect(SCREEN, GREY, rect, 1)
        else:
            pygame.draw.rect(SCREEN, GREY, rect, 0)
