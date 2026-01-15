import math
s = 26+26+10+1
t = math.ceil(math.log(s, 2))
for x in range(1, 320):
    res = (math.ceil(35*t/8+x)*4 + math.ceil(27*t/8+x)*5)
    if res > 320:
        print(x)
        break

