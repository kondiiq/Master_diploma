from random import random
import matplotlib as plx


class Product():
    def __init__(self, name, space, price):
        self.name = name
        self.space = space
        self.price = price


class Individual():
    def __init__(self, spaces, prices, space_limit, generation=0):
        self.spaces = spaces
        self.prices = prices
        self.space_limit = space_limit
        self.score_evaluation = 0
        self.used_space = 0
        self.generation = generation
        self.chromosome = []

        for element in range(len(spaces)):
            if random() < 0.5:
                self.chromosome.append('0')
            else:
                self.chromosome.append('1')

    def fitness(self):
        score = 0
        sum_spaces = 0
        for element in range(len(self.chromosome)):
            if self.chromosome[element] == '1':
                score += self.prices[element]
                sum_spaces += self.spaces[element]
        if sum_spaces > self.space_limit:
            score = 1
        self.score_evaluation = score
        self.used_space = sum_spaces

    def crossover(self, other_individual):
        cutoff = round(random() * len(self.chromosome))
        # print(cutoff)

        child1 = other_individual.chromosome[0:cutoff] + self.chromosome[cutoff::]
        child2 = self.chromosome[0:cutoff] + other_individual.chromosome[cutoff::]
        # print(child1)
        # print(child2)
        children = [Individual(self.spaces, self.prices, self.space_limit, self.generation + 1),
                    Individual(self.spaces, self.prices, self.space_limit, self.generation + 1)]
        children[0].chromosome = child1
        children[1].chromosome = child2
        return children

    def mutation(self, rate):
        # print('Before:', self.chromosome)
        for element in range(len(self.chromosome)):
            if random() < rate:
                if self.chromosome[element] == '1':
                    self.chromosome[element] = '0'
                else:
                    self.chromosome[element] = '1'
        # print('After: ', self.chromosome)
        return self


class GeneticAlgorithm():
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []
        self.generation = 0
        self.best_solution = None
        self.list_of_solutions = []

    def initialize_population(self, spaces, prices, space_limit):
        for element in range(self.population_size):
            self.population.append(Individual(spaces, prices, space_limit))
        self.best_solution = self.population[0]

    def order_population(self):
        self.population = sorted(self.population, key=lambda population: population.score_evaluation, reverse=True)

    def best_individual(self, individual):
        if individual.score_evaluation > self.best_solution.score_evaluation:
            self.best_solution = individual

    def sum_evaluations(self):
        sum = 0
        for individual in self.population:
            sum += individual.score_evaluation
        return sum

    def select_parent(self, sum_evaluation):
        parent = -1
        random_value = random() * sum_evaluation
        sum = 0
        element = 0
        # print('*** random value:', random_value)
        while element < len(self.population) and sum < random_value:
            # print('element:', element, ' - sum: ', sum)
            sum += self.population[element].score_evaluation
            parent += 1
            element += 1
        return parent

    def visualize_generation(self):
        best = self.population[0]
        print('Generation: ', self.population[0].generation,
              'Total price: ', best.score_evaluation, 'Space: ', best.used_space,
              'Chromosome: ', best.chromosome)

    def solve(self, mutation_probability, number_of_generations, spaces, prices, limit):
        self.initialize_population(spaces, prices, limit)

        for individual in self.population:
            individual.fitness()
        self.order_population()
        self.best_solution = self.population[0]
        self.list_of_solutions.append(self.best_solution.score_evaluation)

        self.visualize_generation()

        for generation in range(number_of_generations):
            sum = self.sum_evaluations()
            new_population = []
            for new_individuals in range(0, self.population_size, 2):
                parent1 = self.select_parent(sum)
                parent2 = self.select_parent(sum)
                children = self.population[parent1].crossover(self.population[parent2])
                new_population.append(children[0].mutation(mutation_probability))
                new_population.append(children[1].mutation(mutation_probability))

            self.population = list(new_population)

            for individual in self.population:
                individual.fitness()
            self.visualize_generation()
            best = self.population[0]
            self.list_of_solutions.append(best.score_evaluation)
            self.best_individual(best)

        print('**** Best solution - Generation: ', self.best_solution.generation,
              'Total price: ', self.best_solution.score_evaluation, 'Space: ', self.best_solution.used_space,
              'Chromosome: ', self.best_solution.chromosome)

        return self.best_solution.chromosome


# start program :)

if __name__ == '__main__':
    products_list = []
    products_list.append(Product("Refrigerator A", 0.751, 999.90))
    products_list.append(Product("Cell phone", 0.0000899, 2911.12))
    products_list.append(Product("TV 55' ", 0.400, 4346.99))
    products_list.append(Product("TV 50' ", 0.290, 3999.90))
    products_list.append(Product("TV 42' ", 0.200, 2999.00))
    products_list.append(Product("Notebook A", 0.00350, 2499.90))
    products_list.append(Product("Ventilator", 0.496, 199.90))
    products_list.append(Product("Microwave A", 0.0424, 308.66))
    products_list.append(Product("Microwave B", 0.0544, 429.90))
    products_list.append(Product("Microwave C", 0.0319, 299.29))
    products_list.append(Product("Refrigerator B", 0.635, 849.00))
    products_list.append(Product("Refrigerator C", 0.870, 1199.89))
    products_list.append(Product("Notebook B", 0.498, 1999.90))
    products_list.append(Product("Notebook C", 0.527, 3999.00))
    spaces = []
    prices = []
    names = []
    for product in products_list:
        spaces.append(product.space)
        prices.append(product.price)
        names.append(product.name)
    limit = 3
    population_size = 20
    mutation_probability = 0.05
    number_of_generations = 1000
    ga = GeneticAlgorithm(population_size)
    result = ga.solve(mutation_probability, number_of_generations, spaces, prices, limit)
    print(result)
    for element in range(len(products_list)):
        if result[element] == '1':
            print('Name: ', products_list[element].name, ' - Price: ', products_list[element].price)
    fig, ax = plx.subplots()
    ax.plot(number_of_generations, ga.list_of_solutions)
    ax.set(xlabel='No. Generation', ylabel='Knapsack value', title='Knapsack genetic algorithm')
    ax.grid()
    plx.show()