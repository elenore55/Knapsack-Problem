from random import random
from config import RATE_OF_MUTATION


class Chromosome(object):
    def __init__(self, bit_array, input_data):
        self.bit_array = bit_array
        self._input_data = input_data
        self.fitness = 0
        self._calculate_fitness()

    def __str__(self):
        result = 'Binary code: {0}\nFitness: {1}\nTotal weight: {2}'.format(self.bit_array, self.fitness, self.calculate_total_weight())
        return result

    def __len__(self):
        return len(self.bit_array)

    def mutate(self):
        for i in range(len(self.bit_array)):
            if random() < RATE_OF_MUTATION:
                self.bit_array[i] = self._invert(self.bit_array[i])
        self._calculate_fitness()

    def calculate_total_weight(self):
        total_weight = 0
        for i in range(len(self.bit_array)):
            total_weight += self._input_data.items[i].weight * self.bit_array[i]
        return total_weight

    def _calculate_fitness(self):
        self.fitness = 0
        for i in range(len(self.bit_array)):
            self.fitness += self._input_data.items[i].value * self.bit_array[i]
        if self.calculate_total_weight() > self._input_data.max_capacity:
            self.fitness = 0

    @staticmethod
    def _invert(bit):
        return 1 - bit
