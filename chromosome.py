class Chromosome(object):
    def __init__(self, bit_array, input_data):
        self.bit_array = bit_array
        self._input_data = input_data
        self.fitness = 0
        self.calculate_fitness()

    def calculate_fitness(self):
        total_weight = 0
        for i in range(len(self.bit_array)):
            self.fitness += self._input_data.items[i].value * self.bit_array[i]
            total_weight += self._input_data.items[i].weight * self.bit_array[i]
        if total_weight > self._input_data.max_capacity:
            self.fitness = 0

    def __str__(self):
        return str(self.bit_array) + ' ' + str(self.fitness)
