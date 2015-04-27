class HayStack:
	def __init__(self):
		self.requests = 0

	def get(self, key):
		self.requests += 1
		return key

	def getRequestsNumber(self):
		return self.requests