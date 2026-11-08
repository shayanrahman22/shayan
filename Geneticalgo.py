# # import random
# # import string

# # mutation_rate = 0.01
# # population_size = 150
# # target = "to be or not to be"

# # population = []

# # class DNA:
# #     def __init__(self,length):
# #         self.genes = ''.join(random.choices(string.ascii_lowercase +'',k=length))

# #         self.fitness_score=0

# #     def calculate_fitness(self,target):
# #         self.score =0
# #         for i in range(len(self.genes)):
# #             if population[i]==target[i]:
# #                 self.score += 1
# #         self.fitness_score = self.score /len(target)

# #     def crossover(self,partner):
# #         child = DNA(len(self.genes))

# #         midpoint = random.randint(0,len(self.genes))

# #         for i in range(len(self.genes)):
# #             if (i<midpoint):
# #                 child.genes[i] = self.genes[i]

# #             else:
# #                 child.genes[i]=partner.genes[i]

# #         return child

# #     def mutate(self,mutation_rate):
# #         for i in range(len(self.genes)):
# #             if mutation_rate > random.random():
                




# import random
# import string

# # Mutation rate
# mutation_rate = 0.001

# # Population size
# population_size = 150

# # Target phrase
# target = "shayan is a goood boy"

# # DNA Class
# class DNA:

#     def __init__(self, length):
#         self.genes = ''.join(
#             random.choices(string.ascii_lowercase + ' ', k=length)
#         )
#         self.fitness = 0

#     # Calculate fitness
#     def calculate_fitness(self, target):
#         score = 0
#         for i in range(len(self.genes)):
#             if self.genes[i] == target[i]:
#                 score += 1

#         self.fitness = (score / len(target))

#     # Crossover
#     def crossover(self, partner):

#         child = DNA(len(self.genes))

#         midpoint = random.randint(0, len(self.genes) - 1)

#         child.genes = (
#             self.genes[:midpoint] +
#             partner.genes[midpoint:]
#         )

#         return child

#     # Mutation
#     def mutate(self, mutation_rate):

#         new_genes = list(self.genes)

#         for i in range(len(new_genes)):

#             if random.random() < mutation_rate:
#                 new_genes[i] = random.choice(
#                     string.ascii_lowercase + ' '
#                 )

#         self.genes = ''.join(new_genes)

#     # Get phrase
#     def get_phrase(self):
#         return self.genes


# # Step 1: Initialize Population
# population = []

# for i in range(population_size):
#     population.append(DNA(len(target)))

# generation = 0

# # Genetic Algorithm
# while True:

#     # Step 2: Calculate Fitness
#     for phrase in population:
#         phrase.calculate_fitness(target)

#     # Check whether target is found
#     best = population[0]
#     for val in population:
#         if best.fitness < val.fitness:
#             best = val

#     generation += 1
#     if best.get_phrase() == target:
#         print("Target Found!")
#         print("Generation:", generation)
#         print("Phrase:", best.get_phrase())
#         break

#     # Step 3: Build Mating Pool
#     mating_pool = []

#     for phrase in population:

#         n = int(phrase.fitness * 100)

#         for j in range(n):
#             mating_pool.append(phrase)

#     # Step 4: Reproduction
#     new_population = []

#     for i in range(population_size):

#         if len(mating_pool) == 0:
#             partner_a = random.choice(population)
#             partner_b = random.choice(population)
#         else:
#             partner_a = random.choice(mating_pool)
#             partner_b = random.choice(mating_pool)

#         # Crossover
#         child = partner_a.crossover(partner_b)

#         # Mutation
#         child.mutate(mutation_rate)

#         new_population.append(child)

#     population = new_population

#     # Display progress
#     if generation % 10 == 0:
#         print("Generation:", generation,
#               "Best:", best.get_phrase(),
#               "Fitness:", best.fitness)

import pygame
import random
import math

# --- Configuration & Globals ---
WIDTH, HEIGHT = 640, 240
LIFE_SPAN = 250
life_counter = 0
mutation_rate = 0.01
population_size = 150

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Genetic Algorithm Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 18)

# Target initial position (width / 2, 24)
target = pygame.math.Vector2(WIDTH // 2, 24)

# --- Helper Classes for the Genetic Algorithm ---
class DNA:
    def __init__(self, genes=None):
        if genes:
            self.genes = genes
        else:
            # Create random acceleration vectors for each frame of the life span
            self.genes = []
            for _ in range(LIFE_SPAN):
                angle = random.uniform(0, 2 * math.pi)
                vector = pygame.math.Vector2(math.cos(angle), math.sin(angle))
                vector.scale_to_length(0.2)  # Small force
                self.genes.append(vector)

    def crossover(self, partner):
        new_genes = []
        midpoint = random.randint(0, len(self.genes))
        for i in range(len(self.genes)):
            if i > midpoint:
                new_genes.append(self.genes[i])
            else:
                new_genes.append(partner.genes[i])
        return DNA(new_genes)

    def mutate(self, rate):
        for i in range(len(self.genes)):
            if random.random() < rate:
                angle = random.uniform(0, 2 * math.pi)
                vector = pygame.math.Vector2(math.cos(angle), math.sin(angle))
                vector.scale_to_length(0.2)
                self.genes[i] = vector

class Rocket:
    def __init__(self, dna=None):
        self.position = pygame.math.Vector2(WIDTH // 2, HEIGHT - 20)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.dna = dna if dna else DNA()
        self.fitness_score = 0

    def apply_force(self, force):
        self.acceleration += force

    def update(self):
        # Apply current gene force based on the global life_counter
        if life_counter < len(self.dna.genes):
            self.apply_force(self.dna.genes[life_counter])
        
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0  # Reset acceleration

    def show(self):
        # Draw rocket as a small circle
        pygame.draw.circle(screen, (100, 100, 250), (int(self.position.x), int(self.position.y)), 4)

    def calc_fitness(self):
        # Distance to target (inverse relationship: closer = higher fitness)
        d = self.position.distance_to(target)
        if d < 1: d = 1
        self.fitness_score = 1 / d

class Population:
    def __init__(self, m_rate, num):
        self.mutation_rate = m_rate
        self.rockets = [Rocket() for _ in range(num)]
        self.mating_pool = []
        self.generations = 0

    def live(self):
        for rocket in self.rockets:
            rocket.update()
            rocket.show()

    def fitness(self):
        for rocket in self.rockets:
            rocket.calc_fitness()

    def selection(self):
        self.mating_pool = []
        # Find maximum fitness to normalize values
        max_fit = max(r.fitness_score for r in self.rockets)
        
        # Build mating pool based on relative fitness
        for rocket in self.rockets:
            fitness_normal = rocket.fitness_score / max_fit
            n = int(fitness_normal * 100)  # Arbitrary scaling factor for pool entries
            for _ in range(n):
                self.mating_pool.append(rocket)

    def reproduction(self):
        new_rockets = []
        for _ in range(len(self.rockets)):
            if not self.mating_pool:
                parent_a = Rocket()
                parent_b = Rocket()
            else:
                parent_a = random.choice(self.mating_pool)
                parent_b = random.choice(self.mating_pool)
            
            child_dna = parent_a.dna.crossover(parent_b.dna)
            child_dna.mutate(self.mutation_rate)
            new_rockets.append(Rocket(child_dna))
        
        self.rockets = new_rockets
        self.generations += 1

# Instantiate the population
population = Population(mutation_rate, population_size)

# --- Main Application Loop ---
running = True
while running:
    # 1. Handle Events (Equivalent to mousePressed and exit events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # System adapts to the new target dynamically
            target.x, target.y = pygame.mouse.get_pos()

    # 2. Draw/Render Step (Equivalent to draw() function background)
    screen.fill((255, 255, 255))

    # Draw target: fill(127), stroke(0), stroke_width(2), circle radius 12 (diameter 24)
    pygame.draw.circle(screen, (127, 127, 127), (int(target.x), int(target.y)), 12)
    pygame.draw.circle(screen, (0, 0, 0), (int(target.x), int(target.y)), 12, 2)

    # 3. Evolution Logic
    if life_counter < LIFE_SPAN:
        population.live()
        life_counter += 1
    else:
        life_counter = 0
        population.fitness()
        population.selection()
        population.reproduction()

    # 4. Display Information HUD
    info_text = f"Generation #: {population.generations}\nCycles left: {LIFE_SPAN - life_counter}"
    
    # Split text lines manually since Pygame doesn't render '\n' natively
    y_offset = 20
    for line in info_text.split('\n'):
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (10, y_offset))
        y_offset += 16

    # Refresh screen at 60 FPS
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

