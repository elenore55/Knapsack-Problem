from random import random


class Chromosome(object):
    _RATE_OF_MUTATION = 0.07

    def __init__(self, bit_array, input_data):
        self.bit_array = bit_array
        self._input_data = input_data
        self.fitness = 0
        self._calculate_fitness()

    def __str__(self):
        return str(self.bit_array) + ' ' + str(self.fitness) + ' ' + str(self._calculate_total_weight())

    def __len__(self):
        return len(self.bit_array)

    def mutate(self):
        for i in range(len(self.bit_array)):
            if random() < self._RATE_OF_MUTATION:
                self.bit_array[i] = self._invert(self.bit_array[i])
        self._calculate_fitness()

    def _calculate_fitness(self):
        self.fitness = 0
        for i in range(len(self.bit_array)):
            self.fitness += self._input_data.items[i].value * self.bit_array[i]
        if self._calculate_total_weight() > self._input_data.max_capacity:
            self.fitness = 0

    @staticmethod
    def _invert(bit):
        return 1 - bit

    def _calculate_total_weight(self):
        total_weight = 0
        for i in range(len(self.bit_array)):
            total_weight += self._input_data.items[i].weight * self.bit_array[i]
        return total_weight
