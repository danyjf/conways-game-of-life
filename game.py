from pygame.constants import MOUSEBUTTONDOWN
from grid import Grid
from const import *
import pygame

class Game:    
    def __init__(self):
        pygame.init()
        self.grid = Grid(SCREEN_SIZE[0], SCREEN_SIZE[1])
        
    def mouse_click_event(self):
        pos = pygame.mouse.get_pos()
        idx_x = pos[0] // CELL_SIZE
        idx_y = pos[1] // CELL_SIZE
        
        self.grid.set_alive(idx_x, idx_y)
        
    def game_loop(self):
        running = True
        interactive = True
        while running:
            SCREEN.fill((0, 0, 0))
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
                        
            pygame.display.update()
            
        pygame.quit()
