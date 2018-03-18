# coding=utf-8

# Using t22.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
# by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
# 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import string
from functools import reduce

letters = dict(zip(string.ascii_lowercase, range(1, 27)))
s = reduce(lambda x, y: x + y, open("t22.txt", "r"))
names = sorted(str(s).replace("\"", "").split(","))

whole_sum = 0
for i in range(0, len(names)):
    w = names[i]
    word_sum = 0
    for l in w:
        word_sum += letters.get(str(l).lower())
    whole_sum += word_sum * (i + 1)
print (whole_sum)
