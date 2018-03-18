# print sum(int(x) for x in str(reduce(lambda x, y: x * y, list(range(1, 100)))))
from functools import reduce

print(sum(int(x) for x in str(reduce(lambda x, y: x * y, list(range(1, 100))))))

