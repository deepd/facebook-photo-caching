import collections

class FIFOCache:
    def __init__(self, capacity=50000):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            return self.cache[key]
        except KeyError:
            return -1

    def set(self, key):
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = key