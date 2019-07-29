from itertools import permutations


def prime_dividers(n):
    primes = [n]
    i = 2
    while i * i <= n:
        while n % i == 0:
            n /= i
            primes.append(i)
        i += 1
    primes.append(int(n))
    return set(primes)


def is_prime(n):
    return len(prime_dividers(n)) == 1


sample = []
# for i in range(2, 1000):
for i in range(2, 1000001):
    p = set(map("".join, permutations(str(i))))
    is_circular_prime = all([is_prime(x) for x in {int(x) for x in p}])
    if is_circular_prime:
        sample.append(i)
print(sample)
print(len(sample))
