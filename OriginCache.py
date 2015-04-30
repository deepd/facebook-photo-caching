from FIFOCache import FIFOCache
from LRUCache import LRUCache

class OriginCache:
    def __init__(self, capacity):
        self.cache = FIFOCache(capacity)
        self.misses = 0
        self.hits = 0

    def set(self, key):
    	self.cache.set(key)

    def get(self, key):
        v = self.cache.get(key)
        if v == -1:
            self.misses+=1
        else:
            self.hits+=1
        return v

    def getMisses(self):
    	return self.misses

    def getHits(self):
    	return self.hits