from FIFOCache import FIFOCache

class OriginCache:
	def __init__(self):
        self.cache = FIFOCache()
        self.misses = 0
        self.hits = 0

    def set(self, key):
    	self.cache.set(key)

    def get(self, key):
    	return self.cache.get(key)
