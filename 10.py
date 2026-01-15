import re
file = str(open('10.txt').readlines())
s1 = file.find('ЧАСТЬ ПЕРВАЯ')
s2 = file.find('ЧАСТЬ ВТОРАЯ')
file = file[s1:s2]
f = r'(Браво)'
print(len([x.group() for x in re.finditer(f, file)]))