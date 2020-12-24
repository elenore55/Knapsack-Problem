class Item(object):
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return 'Weight: ' + str(self.weight) + ' Value: ' + str(self.value)
