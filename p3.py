def largest_prime(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n /= i
        i += 1
    return n


n = largest_prime(600851475143)

print(n)
