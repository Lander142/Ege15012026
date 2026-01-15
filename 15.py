res = 0
for a in range(1000):
    for x in range(1000):
        for y in range(1000):
            if ((3*x+y>48) or (x>y) or (4*x+y<a)) == False:
                res = max(res, a)
                break
print(res)