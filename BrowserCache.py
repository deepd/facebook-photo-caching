from LRUCache import LRUCache

class BrowserCache:
	def __init__(self):
        self.cache = LRUCache(5000)
        self.misses = 0
        self.hits = 0

    def set(self, key):
    	self.cache.set(key)

    def get(self, key):
    	return self.cache.get(key)
