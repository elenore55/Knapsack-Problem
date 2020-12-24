class Chromosome(object):
    def __init__(self, all_items, bit_array, max_capacity):
        self.all_items = all_items
        self.bit_arrays = bit_array
        self.max_capacity = max_capacity
        self.fitness = 0

    def calculate_fitness(self):
        pass
