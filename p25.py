x, y, c = 1, 1, 2
while len(str(y)) < 1000:
    x, y = y, x + y
    c += 1
print(c)
