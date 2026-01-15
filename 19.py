def f(n, m):
    if n >= 471: return m % 2 == 0
    if m == 0: return 0
    h = (f(n+4, m-1), f(n+7, m-1), f(n*4, m-1))
    return any(h) if m % 2 == 1 else all(h)
print(len([s for s in range(1, 471) if f(s, 2)]))