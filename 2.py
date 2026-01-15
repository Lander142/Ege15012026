import itertools
def f1(x,y,w,z):
    return (w == x) and (not(y) or z)
def f2(x,y,w,z):
    return not(not(w) or x) or (y==z)
for x1,x2,x3,x4,x5 in itertools.product([0,1], r = 5):
    p = ((1,x1,1,1,1,0),
        (x2,1,0,0,1,x3),
        (x4,0,0,x5,0,0))
    if len(p) == len(set(p)):
        for r in itertools.permutations('xywz', r=4):
            if all(**dict(zip()))