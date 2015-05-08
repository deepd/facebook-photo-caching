import numpy

queries = []

def generateQueries():
	for j in range(0, 70):
		s = numpy.random.zipf(1.15, 1000000)
		for i in s:
			if i <= 1000000:
				queries.append(i)
	return queries