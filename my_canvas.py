# import pygame
# import random

# pygame.init()
# w,h = 800,600
# screen = pygame.display.set_mode((w,h))


# class Perceptron:
#     def __init__(self,inps):
#         self.learning_rate = 0.001

#     def training_data(self):
#         train_data = []

#         for i in range(2000):
#             x = random.randint(-w//2,w//2)
#             y = random.randint(-h//2,h//2)

#             train_data.append([x,y,1])
#         return train_data

#     def f(self,x):
#         return 0.5 * x+1


#     def desired_op(self,x,y):
#         desired = -1

#         if y > self.f(x):
#             desired = 1

#         return desired



# def to_screen(x,y,w,h):
#     screen_x = w//2 + x
#     screen_y = h//2 - y

#     return screen_x,screen_y


# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.update()
    

# pygame.quit()


