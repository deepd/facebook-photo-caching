import collections

class S4LRUCache:
    def __init__(self, capacity=50000):
        self.capacity1 = (int)(capacity/4)
        self.capacity2 = (int)(capacity/4)
        self.capacity3 = (int)(capacity/4)
        self.capacity4 = (int)(capacity/4)
        self.cache1 = collections.OrderedDict()
        self.cache2 = collections.OrderedDict()
        self.cache3 = collections.OrderedDict()
        self.cache4 = collections.OrderedDict()


    def get(self, key):
        try:
            value = self.cache1.pop(key)
            setCache2(key)
            return value
        except KeyError:
            try:
                value = self.cache2.pop(key)
                setCache3(key)
                return value
            except KeyError:
                try:
                    value = self.cache3.pop(key)
                    setCache4(key)
                    return value
                except KeyError:
                    try:
                        value = self.cache4.pop(key)
                        setCache4(key)
                        return value
                    except KeyError:
                        return -1


    def setCache1(self, key):
        if len(self.cache1) >= self.capacity1:
            self.cache1.popitem(last=False)
        self.cache1[key] = key

    def setCache2(self, key):
        if len(self.cache2) >= self.capacity2:
            [k,v] = self.cache2.popitem(last=False)
            setCache1(k)
        self.cache2[key] = key

    def setCache3(self, key):
        if len(self.cache3) >= self.capacity3:
            [k,v] = self.cache3.popitem(last=False)
            setCache2(k)
        self.cache3[key] = key

    def setCache4(self, key):
        if len(self.cache4) >= self.capacity4:
            [k,v] = self.cache4.popitem(last=False)
            setCache3(k)
        self.cache4[key] = key    

