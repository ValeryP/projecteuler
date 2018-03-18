def is_divisible(number, range):
    for n in range:
        if number == 0 or number % n != 0:
            return False
    return True


i = 0
num = 20
while not is_divisible(i, range(1, num + 1)):
    i += num
print(i)
