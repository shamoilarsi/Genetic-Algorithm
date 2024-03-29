import matplotlib.pyplot as plt
import numpy as np
import random
import time

def new_character():
    temp = random.randint(64, 90)
    if temp == 64:
        return chr(32)
    if random.random() > 0.5:
        temp += 32
    return chr(temp)


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
        return max_fitness

    def refill_population(self):
        for i in range(0, self.max_pop):
            gene_a = random.choice(self.mating_pool)
            gene_b = random.choice(self.mating_pool)

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
        print("\nTarget String : " + self.target)
        print("Total Population : " + str(self.max_pop))
        print("Mutation Rate : " + str(self.mutation_rate))
        print("Average Fitness : " + str("{:0.5f}".format(self.average_fitness())))
        print("Total Generations : " + str(self.generation))


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

def main():
    # Currently only supports Capital letters, small letters and spaces.
    target = "To Be Or Not To Be"
    max_pop = 1000
    mutationRate = 0.01
    time_array = []
    fitness_array = []

    millis = int(time.time() * 1000)
    my_algorithm = Population(target, max_pop, mutationRate)
    my_algorithm.calc_fitness()

    while not my_algorithm.finished:
        max_fitness = my_algorithm.natural_selection()  # aka generating mating pool according to probability
        my_algorithm.refill_population()
        my_algorithm.calc_fitness()
        print(str(" ".join(my_algorithm.evaluate())))

        fitness_array.append(max_fitness * 100)
        time_array.append(int(time.time() * 1000) - millis)

    plt.plot(time_array, fitness_array)   
    plt.xlabel('Time') 
    plt.ylabel('Max Fitness')
    plt.title('Fitness Graph')

    my_algorithm.fully_evolved()
    print("Total Time : " + str(int(time.time() * 1000) - millis))
    plt.show() 

    
if __name__ == "__main__":
    main()
