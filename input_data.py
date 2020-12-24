from item import Item


class InputData(object):
    _PATH = 'data_knapsack01.txt'

    def __init__(self):
        self.max_capacity = 0
        self.items = []
        self._load()

    def _load(self):
        file = open(self._PATH, 'r')
        lines = [line.strip() for line in file]
        header = lines[0].split()
        self.max_capacity = int(header[1])
        for i in range(1, len(lines)):
            [weight, value] = lines[i].split(',')
            self.items.append(Item(weight, value))
