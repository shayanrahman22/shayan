import numpy as np
import pygame

w,h = 1000,850
pygame.init()
screen = pygame.display.set_mode((w,h))


cell_size = 10
rows = h // cell_size
cols = w// cell_size

grid = np.zeros((rows,cols))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    for row in range(rows):
        for col in range(cols):

            x = col * cell_size
            y = row * cell_size

            if grid[row][col] == 0:
                color = (0, 0, 0)
            else:
                color = (255, 255, 255)

            pygame.draw.rect(
            screen,
            color,
            (x, y, cell_size, cell_size)
            )
    for row in range(rows):
        for col in range(cols):
            x = col * cell_size
            y = row * cell_size

            if grid[x][y]==0:
                
            
    pygame.display.update()






