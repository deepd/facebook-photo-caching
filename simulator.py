import genzipf
from EdgeCache import EdgeCache
from OriginCache import OriginCache
from HayStack import HayStack
from FIFOCache import FIFOCache
from LRUCache import LRUCache
from LFUCache import LFUCache
from S4LRUCache import S4LRUCache
import random

def getOrigin(req):
	return req%4

def fetch(req, edge, origin, hay):
	backPopulate = []
	r = random.randint(0, 8) 
	value1 = edge[r].get(req)
	if value1 == -1:
		backPopulate.append(edge[r])
		o = getOrigin(req)
		value2 = origin[o].get(req)
		if value2 == -1:
			backPopulate.append(origin[o])
			value3 = hay.get(req)
	for obj in backPopulate:
		obj.set(req)

def printResults(reqs, edge, origin, hay):
	hits = 0
	misses = 0
	count = 0
	for e in edge:
		hits += e.getHits()
		misses += e.getMisses()
	print "Edge percent traffic : ", (hits*100.0)/reqs
	print "Edge Hit-ratio : ", (hits*100.0)/(hits+misses)
	print "*********"

	hits = 0
	misses = 0
	for e in origin:
		hits += e.getHits()
		misses += e.getMisses()
	print "Origin percent traffic : ", (hits*100.0)/reqs
	print "Origin Hit-ratio : ", (hits*100.0)/(hits+misses)
	print "*********"
	
	hits = 0
	misses = 0
	hits += hay.getRequestsNumber()
	print "HayStack percent traffic : ", (hits*100.0)/reqs
	print "HayStack Hit-ratio : ", (hits*100.0)/(hits+misses)
	print "*********"

if __name__ == "__main__":
	edge = [EdgeCache(FIFOCache(2000)) for i in range(0,9)]
	origin = [OriginCache(FIFOCache(5000)) for i in range(0,4)]
	hay = HayStack()
	requests = genzipf.generateQueries()
	for req in requests:
		fetch(req, edge, origin, hay)
	printResults(len(requests), edge, origin, hay)
