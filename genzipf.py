import numpy

queries = []

def generateQueries():
	for j in range(0, 100):
		s = numpy.random.zipf(1.9, 1000000)
		for i in s:
			if i <= 1000000:
				queries.append(i)
	return queries