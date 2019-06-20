import random


def new_character():
    temp = random.randint(64, 90)
    if temp == 64:
        return chr(32)
    if random.random() > 0.5:
        temp += 32
    return chr(temp)


class DNA:
    def __init__(self, target_length):
        self.genes = []  # Or also known as the array of characters
        self.fitness = 0

        for i in range(target_length):
            self.genes.append(new_character())

    def calc_fitness(self, target):
        self.fitness = 0
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                self.fitness += 1
        self.fitness /= len(target)
        # self.fitness = self.fitness ** len(target)

    def crossover(self, gene_b):
        child = DNA(len(gene_b.genes))

        midpoint = random.randint(0, len(gene_b.genes))
        for i in range(len(gene_b.genes)):
            if i < midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = gene_b.genes[i]

        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = new_character()
