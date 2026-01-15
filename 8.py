import sys
from functools import lru_cache
sys.setrecursionlimit(100000000)
@lru_cache(None)
def f(n):
    if n == 100:
        return 1
    if n > 100:
        return 0
    return f(n+1) + f(n+2) + f(n+5) + f(n+10)
print(f(0))