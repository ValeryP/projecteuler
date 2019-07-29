# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def is_polyndrom(n):
    binary_str_n, str_n = str(bin(n))[2:], str(n)
    return str_n == str_n[::-1] and binary_str_n == binary_str_n[::-1]


print(sum([x for x in range(1, 1000001) if is_polyndrom(x)]))
