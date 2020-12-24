from chromosome import Chromosome
from random import choice, random, randrange


class Population(object):
    _ELITISM = 10

    def __init__(self, input_data, size=650):
        self._input_data = input_data
        self._size = size
        self.chromosomes = []

    def generate_initial_population(self):
        for i in range(self._size):
            self.chromosomes.append(self._generate_random_chromosome())

    def get_max_fitness(self):
        return max([c.fitness for c in self.chromosomes])

    def get_end_result(self):
        self.rank_chromosomes()
        return self.chromosomes[-1]

    def calculate_similarity(self):
        abs_sum = 0
        for i in range(self._size - 1):
            abs_sum += abs(self.chromosomes[i].fitness - self.chromosomes[i + 1].fitness)
        return abs_sum / (self._size - 1)

    def rank_chromosomes(self):
        self.chromosomes = sorted(self.chromosomes, key=lambda c: c.fitness)

    def generate_new_population(self):
        self.rank_chromosomes()
        elite = self.get_elite_members()
        children = self.generate_children()
        self.chromosomes = elite + children

    def get_elite_members(self):
        return self.chromosomes[-self._ELITISM:]

    def generate_children(self):
        children = []
        for i in range(0, self._size - self._ELITISM, 2):
            parents = self.choose_pair_of_parents()
            children_pair = self.crossover(parents)
            children.append(children_pair[0])
            children.append(children_pair[1])
        return children

    def crossover(self, parents):
        index = randrange(len(parents) - 1)
        child1 = Chromosome(parents[0].bit_array[:index] + parents[1].bit_array[index:], self._input_data)
        child2 = Chromosome(parents[1].bit_array[:index] + parents[0].bit_array[index:], self._input_data)
        child1.mutate()
        child2.mutate()
        return [child1, child2]

    def choose_pair_of_parents(self):
        max_val1 = float('-inf')
        index1 = 0
        max_val2 = float('-inf')
        index2 = 0
        for i in range(self._size):
            score = (i + 1) * random()
            if score > max_val1:
                max_val1, max_val2 = score, max_val1
                index1, index2 = i, index1
            elif score > max_val2:
                max_val2 = score
                index2 = i
        return [self.chromosomes[index1], self.chromosomes[index2]]


    def _generate_random_chromosome(self):
        num_of_bits = len(self._input_data.items)
        bit_array = []
        bits = [0, 1]
        for i in range(num_of_bits):
            bit_array.append(choice(bits))
        return Chromosome(bit_array, self._input_data)
