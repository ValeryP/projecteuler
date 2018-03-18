def basic():
    f = open("t13.txt", "r")
    sum = 0
    for line in f:
        sum += int(line)
    print(str(sum)[:10])


basic()
