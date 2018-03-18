def basic():
    number = 13
    longest = {}
    while number < 1000000:
        chain = [number]
        s = str(number)
        n = number
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
            s += " -> %d" % n
            chain.append(n)
        longest[len(chain)] = number
        number += 1
        print(number)
    print(longest.get(list(reversed(longest.keys()))[0]))


basic()
