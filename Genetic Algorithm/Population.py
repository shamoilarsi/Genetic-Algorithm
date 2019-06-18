import math
import random

from DNA import DNA


class Population:
    def __init__(self, target, max_pop, mutation_rate):
        self.target = target
        self.max_pop = max_pop
        self.mutation_rate = mutation_rate
        self.population_array = []
        self.mating_pool = []
        self.finished = False
        self.generation = 0

        for i in range(max_pop):
            self.population_array.append(DNA(len(self.target)))

    def calc_fitness(self):
        for i in range(self.max_pop):
            self.population_array[i].calc_fitness(self.target)

    def natural_selection(self):  # aka generating mating pool
        self.mating_pool = []
        max_fitness = 0

        for i in range(self.max_pop):
            if self.population_array[i].fitness > max_fitness:
                max_fitness = self.population_array[i].fitness

        for i in range(self.max_pop):
            n = int((self.population_array[i].fitness / max_fitness) * len(self.target))
            for j in range(n):
                self.mating_pool.append(self.population_array[i])

    def refill_population(self):
        for i in range(0, self.max_pop):
            gene_a = self.mating_pool[math.floor(random.randint(0, len(self.mating_pool) - 1))]
            gene_b = self.mating_pool[math.floor(random.randint(0, len(self.mating_pool) - 1))]

            gene_child = gene_a.crossover(gene_b)
            gene_child.mutate(self.mutation_rate)
            self.population_array[i] = gene_child
        self.generation += 1

    def evaluate(self):
        max_fitness = 0
        index = 0
        for i in range(self.max_pop):
            if self.population_array[i].fitness > max_fitness:
                max_fitness = self.population_array[i].fitness
                index = i

        if max_fitness == 1:
            self.finished = True

        return self.population_array[index].genes

    def average_fitness(self):
        total_fitness = 0
        for i in range(0, self.max_pop):
            total_fitness += self.population_array[i].fitness
        return total_fitness / self.max_pop

    def fully_evolved(self):
        print("Target String : " + self.target)
        print("Total Population : " + str(self.max_pop))
        print("Mutation Rate : " + str(self.mutation_rate))
        print("Average Fitness : " + str("{:0.5f}".format(self.average_fitness())))
        print("Total Generations : " + str(self.generation))
