from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['a'].append(4)

print(d)