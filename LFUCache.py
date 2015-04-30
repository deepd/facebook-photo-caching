import collections

class LFUCache:
    def __init__(self, capacity=50000):
        self.capacity = capacity
        self.lfu = {}
        self.min = 0

    def get(self, key):
        if key in self.lfu:
            self.lfu[key] += 1
            return key
        return -1

    def set(self, key):
        if len(self.lfu) >= self.capacity:
            # find the LFU entry
            #old_key = min(self.lfu.keys(), key=lambda k:self.lfu[k])
            self.lfu.pop(self.min)
        self.lfu[key] = 1
        self.min = key

