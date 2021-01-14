from item import Item
from config import DATA_PATH


class InputData(object):
    def __init__(self):
        self.max_capacity = 0
        self.items = []
        self._load()

    def _load(self):
        file = open(DATA_PATH, 'r')
        lines = [line.strip() for line in file]
        header = lines[0].split()
        self.max_capacity = int(header[1])
        for i in range(1, len(lines)):
            [weight, value] = lines[i].split(',')
            self.items.append(Item(int(weight), int(value)))
