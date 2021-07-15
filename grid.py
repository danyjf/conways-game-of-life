from const import CELL_SIZE
import pygame
from pygame.constants import WINDOWHITTEST
from cell import Cell

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.initialize_grid()
        self.alive = []
        
    def initialize_grid(self):
        grid = []
        for y in range(0, self.height, CELL_SIZE):
            grid.append([])
            for x in range(0, self.width, CELL_SIZE):
                grid[y // CELL_SIZE].append(Cell(x, y))
            
        # set neighbours of each cell
        for row in grid:
            for cell in row:
                cell.set_neighbours(grid)
        
        return grid
    
    def set_alive(self, idx_x, idx_y):
        cell = self.grid[idx_y][idx_x]
        if cell not in self.alive:
            cell.is_alive = True
            cell.draw()
            self.alive.append(cell)
        
    def set_dead(self, idx_x, idx_y):
        cell = self.grid[idx_y][idx_x]
        if cell in self.alive:
            cell.is_alive = False
            cell.draw()
            self.alive.remove(cell)

    def draw(self):
        for y in range(0, self.height, CELL_SIZE):
            for x in range(0, self.width, CELL_SIZE):
                self.grid[y // CELL_SIZE][x // CELL_SIZE].draw()
