res = 0
for i in range(1, 10000):
    s = bin(i)[2:]
    if i % 5 == 0:
        s = '1' + s + s[-2] + s[-1]
    else:
        s = bin(i%5)[2:] + s
    r = int(s, 2)
    if r <= 223:
        res = max(res, r)
print(res)