v = 2
l = [1]
while v < 4000000:
    l.append(v)
    v = l[len(l) - 1] + l[len(l) - 2]
print(sum(list(filter(lambda x: x % 2 == 0, l))))
