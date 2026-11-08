import pygame 
import math
from pygame import Vector2
import random as rd

pygame.init()


running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            