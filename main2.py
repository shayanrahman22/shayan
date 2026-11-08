import pygame
import sys
import random 
from pygame import Vector2
import copy
import math

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Random Rocket")

class rocket:
    def __init__(self,vertex):
        self.vertex = vertex
        
        self.position = Vector2()
        self.sum_x = 0
        self.sum_y = 0
        for i in range(len(vertex)):
            self.sum_x +=vertex[i].x  
            self.sum_y += vertex[i].y

        self.position.x=self.sum_x/len(self.vertex) #calculating the position vector
                                                     #by adding vertex and dividing by length of vertex
        self.position.y=self.sum_y/len(self.vertex) 
        self.relative_vec=[]

        for i in range(len(self.vertex)):
            self.relative_vec.append(self.vertex[i]-self.position) #relative vector = each vertex(means single vertex) - position vector 
        self.velocity = Vector2(random.randint(-3,3),random.randint(-3,3))


    
    def move(self):
        self.acc_vec=Vector2(random.uniform(-0.1, 0.1),random.uniform(-0.1, 0.1))
        self.velocity += self.acc_vec
         

        self.new_pos = self.velocity + self.position
        self.position = self.new_pos

        self.angle_rd = math.atan2(self.velocity.y,self.velocity.x)
        self.angle_dg = math.degrees(self.angle_rd)

        self.rtd_rel_vec =[]
        for i in range(len(self.vertex)):
            self.rtd_rel_vec.append(self.relative_vec[i].rotate(self.angle_dg))

        self.actual_pos = []
        for i in range(len(self.vertex)):
            self.actual_pos.append(self.new_pos+self.rtd_rel_vec[i])#actual_vertex = new_position + relative_vertex

        if self.new_pos.x < 0:
            self.new_pos.x = 0
            self.velocity.x *= -1  # Reverse horizontal direction
        elif self.new_pos.x > 1000:
            self.new_pos.x = 1000
            self.velocity.x *= -1

        # Height boundary (0 to 700)
        if self.new_pos.y < 0:
            self.new_pos.y = 0
            self.velocity.y *= -1  # Reverse vertical direction
        elif self.new_pos.y > 700:
            self.new_pos.y = 700
            self.velocity.y *= -1
            

        return self.actual_pos



    
population = 150
tri = [ Vector2(500, 375), Vector2(492.5, 400), Vector2(507.5, 400) ]

clock = pygame.time.Clock()

population_l  = []


for i in range(population):
    population_l.append(rocket(copy.deepcopy(tri)))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((15,15,20))

    for rk in population_l:
       pygame.draw.polygon(screen,(250,0,0),rk.move())
       

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()



 