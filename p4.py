s = set()
f = 100
t = 1000
for i in range(f, t):
    for j in range(f, t):
        s.add(j * i)
mx = 1
for i in list(s):
    if i > mx and str(i) == str(i)[::-1]:
        mx = i
print(mx)
