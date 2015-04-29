import genzipf
import EdgeCache
import OriginCache
import HayStack


def fetch(req, edge, origin, hay):
	

def printResults(reqs, edge, origin, hay):
	hits = 0
	misses = 0
	for e in edge:
		hits += e.getHits()
		misses += e.getMisses()
	print "Edge Hit-ratio : ", (hits/reqs)*100
	hits = 0
	misses = 0
	for e in origin:
		hits += e.getHits()
		misses += e.getMisses()
	print "Origin Hit-ratio : ", (hits/reqs)*100
	hits = 0
	misses = 0
	for e in hay:
		hits += e.getRequestsNumber()
	print "HayStack Hit-ratio : ", (hits/reqs)*100

if __name__ == "__main__":
	edge = [EdgeCache() for i in range(0,9)]
	origin = [OriginCache() for i in range(0,4)]
	hay = HayStack()
	requests = genzipf.generateQueries()
	for req in requests:
		fetch(req, edge, origin, hay)
	printResults(len(requests), edge, origin, hay)
