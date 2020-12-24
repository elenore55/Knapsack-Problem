from chromosome import Chromosome
from random import choice


class Population(object):
    def __init__(self, input_data, size=200):
        self._input_data = input_data
        self._size = size
        self.chromosomes = []

    def generate_initial_population(self):
        for i in range(self._size):
            self.chromosomes.append(self._generate_random_chromosome())

    def rank_chromosomes(self):
        sorted(self.chromosomes, key=lambda c: c.fitness)

    def _generate_random_chromosome(self):
        num_of_bits = len(self._input_data.items)
        bit_array = []
        bits = [0, 1]
        for i in range(num_of_bits):
            bit_array.append(choice(bits))
        return Chromosome(bit_array, self._input_data)
