from math import pow

n = 5
match = []
for x in range(2, 9999999):
    if x == sum([pow(int(v), n) for v in str(x)]):
        match.append(x)
print(match, sum(match))
