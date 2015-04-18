import numpy as np

s = np.random.zipf(1.9, 1000000)
f = open('queries', 'w')
for i in s:
	if i <= 1000000:
		f.write(str(i))
		f.write('\n')
print min(s), max(s)