# coding=utf-8

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

a_sum = 0
for i in range(1, 10000):
    s = sum([x for x in range(1, i) if i % x == 0])
    if sum([x for x in range(1, s) if s % x == 0]) == i and i != s:
        print('%d : %d' % (i, s))
        a_sum += s + i
print(a_sum / 2)  # because we sum numbers twice
# 220 : 284
# 284 : 220 !!
# 1184 : 1210
# 1210 : 1184 !!
