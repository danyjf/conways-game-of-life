from os import kill
from pygame.constants import MOUSEBUTTONDOWN
from grid import Grid
from const import *
import pygame
import time

class Game:    
    def __init__(self):
        pygame.init()
        self.grid = Grid(SCREEN_SIZE[0], SCREEN_SIZE[1])
        self.clock = pygame.time.Clock()
        
    def mouse_click_event(self):
        pos = pygame.mouse.get_pos()
        idx_x = pos[0] // CELL_SIZE
        idx_y = pos[1] // CELL_SIZE
        
        if self.grid.grid[idx_y][idx_x].is_alive:
            self.grid.set_dead(idx_x, idx_y)
        else:
            self.grid.set_alive(idx_x, idx_y)
        
    def live_neighbours(self, cell):
        n = 0
        
        for neighbour in cell.neighbours:
            if neighbour.is_alive:
                n += 1
                
        return n
        
    def algorithm(self):
        alive = []
        dead = []
        # print(self.grid.alive)
        # alive = self.grid.alive.copy()
        for cell in self.grid.alive:
            # print('mine', alive)
            # print('grid', self.grid.alive)
            idx_x = cell.x // CELL_SIZE
            idx_y = cell.y // CELL_SIZE
            
            n_live = self.live_neighbours(cell)
            if n_live < 2 or n_live > 3:
                dead.append((idx_x, idx_y))
                # self.grid.set_dead(idx_x, idx_y)
            
            for nb in cell.neighbours:
                if not nb.is_alive:
                    n_live = self.live_neighbours(nb)
                    # print('live', n_live)
                    if n_live == 3 and (nb.x // CELL_SIZE, nb.y // CELL_SIZE) not in alive:
                        # print('here')
                        alive.append((nb.x // CELL_SIZE, nb.y // CELL_SIZE))
                        # self.grid.set_alive(nb.x // CELL_SIZE, nb.y // CELL_SIZE)
            
        # print('set alive:', alive)
        # print('set dead:', dead)

        for t in alive:
            self.grid.set_alive(t[0], t[1])
        for t in dead:
            self.grid.set_dead(t[0], t[1])
        
    def game_loop(self):
        running = True
        interactive = True
        while running:
            self.grid.draw()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if interactive:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_click_event()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        interactive = False
                elif not interactive:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        interactive = True

            if not interactive:
                self.algorithm()
                self.clock.tick(2)
                        
            pygame.display.update()
            
        pygame.quit()
