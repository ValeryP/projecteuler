# def prime_numbers(n):
#     primes = []
#     i = 2
#     while i * i < n:
#         while n % i == 0:
#             n /= i
#             primes.append(i)
#         i += 1
#     primes.append(int(n))
#     return primes


def largest_prime(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n /= i
        i += 1
    return n


def is_smooth(n):
    l_prime = largest_prime(n)
    return l_prime * l_prime <= n


res = [x for x in range(1, 1000000) if is_smooth(x)]
# res = [x for x in range(1, 10000000000) if is_smooth(x)]
# for r in range(1, 100):
#     print(f'{r}: {prime_numbers(r)[-1]} < {math.sqrt(r)}')
# print(res)
print(len(res))
