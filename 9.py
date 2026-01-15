file = open('9.csv')
s = [list(map(int, i.split('\n')[0].split(';'))) for i in file]
cnt = 0
for i in s:
    if i[0] != min(i) and i[-1] != max(i) and i[0] != max(i) and i[-1] != min(i):
        if (i[0]-i[-1]) != 0 and (max(i)-min(i)) % (i[0]-i[-1]) == 0:
            cnt += 1
print(cnt)