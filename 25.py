def f(n):
    t = 12
    while t < n:
        if n % t == 0 and str(t)[-2:] == '11':
            return t
        t += 1
    return 0
cnt = 0
for i in range(1_350_050, 10_000_000):
    if f(i):
        print(i, f(i))
        cnt += 1
    if cnt == 5:
        break
