file = open('17.txt')
s = [int(x) for x in file]
max13 = 0
for i in s:
    if len(str(i)) >= 2:
        if str(i)[-2:] == '13':
            max13 = max(max13, i)
res = []
for i in range(len(s)-2):
    x1 = s[i]
    x2 = s[i+1]
    x3 = s[i+2]
    if ((len(str(x1)) == 3) + (len(str(x2)) == 3) + (len(str(x3)) == 3)) == 2:
        if x1+x2+x3 <= max13:
            res.append(x1+x2+x3)
print(len(res), max(res))
