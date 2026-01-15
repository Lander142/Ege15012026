for i in range(1, 500):
    s = '0' * i + '1' * i + '2' * (1000-2*i)
    s1 = []
    r1 = 0
    for j in s:
        r1 += int(j)
        if j == '0':
            s1.append(1)
        elif j == '1':
            s1.append(2)
        elif j == '2':
            s1.append(0)
    if r1 - sum(s1) == 200:
        print(1000-2*i)
        break