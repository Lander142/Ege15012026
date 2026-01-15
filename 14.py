def seven(n):
    s = ''
    while n > 0:
        s += str(n%7)
        n //= 7
    return s[::-1]
s = seven(5*343**8+4*49**12+7**14-98)
d = dict()
maxx = 0
for i in s:
    if i not in d:
        d[i] = 0
    else:
        d[i] += 1
    if d[i] > maxx:
        maxx = d[i]
        ans = i
print(ans)