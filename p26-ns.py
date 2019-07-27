import re
from decimal import Decimal

repetitions = dict()
for x in range(2, 1000):
    dd = Decimal(1 / x)
    d = str(dd).split('.')[1]
    search = re.compile(r'(.+?.+?)(\1)+?').search(d)
    if search:
        l = len(search.group(1))
        if l in repetitions:
            repetitions[l].append((x, dd))
        else:
            repetitions[l] = [(x, dd)]
# print(x, dd, search.group(1))

# print(repetitions)
print(repetitions[max(repetitions.keys())], max(repetitions.keys()))
