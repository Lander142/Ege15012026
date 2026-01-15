file = open('18.csv').read()
s = (file.split('\n'))
ls = [list(map(int, i.split(' '))) for i in s[:-1]]
mn = float('INF')
mx = float('-INF')
for i in range(len(ls)):
    for j in range(len(ls[i])):
        x = i
        y = j
        s = ls[x][y]
        flag = True
        for _ in range(2):
            y+=1
            if y > len(ls[i]) - 1:
                flag = False
                break
            s += ls[x][y]
        if flag == False:
            continue
        for _ in range(5):
            x+=1
            if x > len(ls)-1:
                flag = False
                break
            s += ls[x][y]
        if flag == False:
            continue
        for _ in range(5):
            y -= 1
            if y < 0:
                flag = False
                break
            s += ls[x][y]
        if flag == False:
            continue
        for _ in range(5):
            x-=1
            if x < 0:
                flag = False
                break
            s += ls[x][y]
        if flag == False:
            continue
        mx = max(s, mx)
        mn = min(s, mn)
print(mx, mn)
