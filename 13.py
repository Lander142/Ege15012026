mask = [255,255,255,224]
ip = [116,242,1,26]
for i in mask:
    print((8-len(bin(i)[2:]))*'0'+bin(i)[2:], end=' ')
print()
for i in ip:
    print((8-len(bin(i)[2:]))*'0'+bin(i)[2:], end=' ')
print()
for i in range(4):
    s = ip[i]&mask[i]
    print((8-len(bin(s)[2:]))*'0'+bin(s)[2:], end=' ')
for a in range(0, 255):

    mask = [255,255,255,224]
    ip = [116,242,a,26]