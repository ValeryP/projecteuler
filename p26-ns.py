import re
from decimal import Decimal

# https://en.wikipedia.org/wiki/Repeating_decimal?oldformat=true#Decimal_expansion_and_recurrence_sequence
repetitions = dict()
for x in range(2, 1000):
    dd = Decimal(1 / x)
    d = str(dd).split('.')[1]
    search = re.findall(r'(.+?.+?)(\1)+?', d)
    if search:
        l = sum([len(y) for x in search for y in x]) / 2
        if l in repetitions:
            repetitions[l].append((x, dd, search))
        else:
            repetitions[l] = [(x, dd, search)]

longest = max(repetitions.keys())
print(repetitions[longest], longest)
