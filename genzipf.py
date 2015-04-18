import numpy as np

f = open('queries', 'w')


for j in range(0, 100):
	s = np.random.zipf(1.9, 1000000)
	for i in s:
		if i <= 1000000:
			f.write(str(i))
			f.write('\n')