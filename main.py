import pygame
import sys
import random as rd
import numpy as np
import math



pygame.init()

width = 1000
height = 700

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("AI survival game")

clock = pygame.time.Clock()

player =pygame.Rect(375,500,50,50)
speed = 5
e_speed = 2.5


enemies = [
    pygame.Rect(200, 150, 40, 40),
    pygame.Rect(500, 200, 40, 40),
    pygame.Rect(800, 350, 40, 40),
    pygame.Rect(150, 450, 40, 40)
]

running = True
while running:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed


    for enemy in enemies:
        pos_vect = [player.x-enemy.x,player.y-enemy.y]
        mag = np.linalg.norm(pos_vect)
        if mag ==0:
            mag = 1

        pos_vect = pos_vect[0]/mag , pos_vect[1]/mag
        velo_vec = [pos_vect[0]*e_speed,pos_vect[1]*e_speed]



        enemy.x,enemy.y=enemy.x+velo_vec[0],enemy.y+velo_vec[1]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        


    screen.fill((15,15,20))
    pygame.draw.rect(screen,(0,255,0),player)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

        
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()