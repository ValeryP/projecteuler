n = 100
l1 = sum(list(map(lambda x: x ** 2, range(1, n + 1))))
l2 = sum(range(1, n + 1)) ** 2
print(l2 - l1)
