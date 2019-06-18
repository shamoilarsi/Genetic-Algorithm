from Population import Population

# Currently only supports Capital letters, small letters and spaces.
target = "To Be Or Not To Be"
max_pop = 100
mutationRate = 0.01

my_algorithm = Population(target, max_pop, mutationRate)
my_algorithm.calc_fitness()

while not my_algorithm.finished:
    my_algorithm.natural_selection()  # aka generating mating pool according to probability
    my_algorithm.refill_population()
    my_algorithm.calc_fitness()
    print(str(my_algorithm.evaluate()))

my_algorithm.fully_evolved()