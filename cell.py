import pygame
from const import *

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = False
        self.neighbours = []
        
    def set_neighbours(self, grid):
        x = self.x // CELL_SIZE
        y = self.y // CELL_SIZE
        
        if x-1 >= 0:
            self.neighbours.append(grid[y][x-1])
            if y-1 >= 0:
                self.neighbours.append(grid[y-1][x-1])
            if y+1 <= len(grid)-1:
                self.neighbours.append(grid[y+1][x-1])
        if x+1 <= len(grid[0])-1:
            self.neighbours.append(grid[y][x+1])
            if y-1 >= 0:
                self.neighbours.append(grid[y-1][x+1])
            if y+1 <= len(grid)-1:
                self.neighbours.append(grid[y+1][x+1])
        if y-1 >= 0:
            self.neighbours.append(grid[y-1][x])
        if y+1 <= len(grid)-1:
            self.neighbours.append(grid[y+1][x])

    def draw(self):
        rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)
        if not self.is_alive:
            pygame.draw.rect(SCREEN, WHITE, rect, 0)
            pygame.draw.rect(SCREEN, GREY, rect, 1)
        else:
            pygame.draw.rect(SCREEN, BLACK, rect, 0)
            pygame.draw.rect(SCREEN, GREY, rect, 1)
            
    def __repr__(self):
        return '(' + str(self.x // CELL_SIZE) + ', ' + str(self.y // CELL_SIZE) + ')'
