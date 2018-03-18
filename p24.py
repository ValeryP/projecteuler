# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
# 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
#  The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import random
import math
from joblib import Parallel, delayed
import multiprocessing

n = 10
l = list(range(n))
c = []
se = set()
f = math.factorial(n)
num_cores = multiprocessing.cpu_count()


def count():
    while len(c) < f:
        random.shuffle(l)
        r = "".join(str(s) for s in l)
        if r not in se:
            c.append(r)
            se.add(r)
            print("%.2f" % (len(c) / f * 100) + "%")
    print(sorted(c)) #todo save in file and ONLY after work with it


results = Parallel(n_jobs=num_cores)(delayed(count())) #todo does not work
