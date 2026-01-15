cnt = 0
for x1 in range(101):
    for x2 in range(51):
        for x5 in range(21):
            for x10 in range(11):
                if x1 + x2*2 + x5*5 + x10*10 == 100:
                    cnt+=1
print(cnt)