class OriginCache:
	def __init__(self, cache_type):
        self.cache = cache_type
        self.misses = 0
        self.hits = 0

    def set(self, key):
    	self.cache.set(key)

    def get(self, key):
    	return self.cache.get(key)

    def getMisses(self):
    	return self.misses

    def getHits(self):
    	return self.hits