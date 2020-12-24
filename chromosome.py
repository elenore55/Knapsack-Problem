from random import random, randrange
from copy import deepcopy


class Chromosome(object):
    _RATE_OF_MUTATION = 0.07

    def __init__(self, bit_array, input_data):
        self.bit_array = bit_array
        self._input_data = input_data
        self.fitness = 0
        self.calculate_fitness()

    def calculate_fitness(self):
        self.fitness = 0
        total_weight = 0
        for i in range(len(self.bit_array)):
            self.fitness += self._input_data.items[i].value * self.bit_array[i]
            total_weight += self._input_data.items[i].weight * self.bit_array[i]
        if total_weight > self._input_data.max_capacity:
            self.fitness = 0

    def __str__(self):
        return str(self.bit_array) + ' ' + str(self.fitness) + ' ' + str(self._total_w())

    def __len__(self):
        return len(self.bit_array)

    def mutate(self):
        for i in range(len(self.bit_array)):
            if random() < self._RATE_OF_MUTATION:
                self.bit_array[i] = self._invert(self.bit_array[i])
        self.calculate_fitness()

    def mutate2(self):
        r1 = randrange(len(self.bit_array) - 1)
        r2 = randrange(len(self.bit_array) - 1)
        if r2 < r1:
            r1, r2 = r2, r1
        mutated = self.bit_array[:r1] + self.bit_array[r1:r2][::-1] + self.bit_array[r2:]
        self.bit_array = deepcopy(mutated)
        self.calculate_fitness()

    @staticmethod
    def _invert(bit):
        return 1 - bit

    def _total_w(self):
        total_weight = 0
        for i in range(len(self.bit_array)):
            total_weight += self._input_data.items[i].weight * self.bit_array[i]
        return total_weight
