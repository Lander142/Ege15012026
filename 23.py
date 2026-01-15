def f(n, m):
    if n < m or n == 40:
        return 0
    if n == m:
        return 1
    return f(n-3, m) + f(n//2, m) + f(n//5, m)
print(f(120, 49)*f(49, 6))