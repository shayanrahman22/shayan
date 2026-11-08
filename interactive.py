import random as rd

class DNA:
    def __init__(self):
        self.genes = []
        for i in range(14):
            self.genes = rd.uniform(0,1)


class Flower:
    def __init__(self,dna):
        self.dna = dna
        self.fitness = 1

        