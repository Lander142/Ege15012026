from turtle import *
screensize(3000,3000)
tracer(0)
k = 30
x = 0
y = 0
cnt = 0
for _ in range(10):
    x += 4
    y += 3
    setpos(x*k, y*k)
    x -= 4
    y += 10
    setpos(x*k, y*k)
    x += 18
    y -= 12
    setpos(x*k, y*k)
    x -= 24
    y -= 12
    setpos(x*k, y*k)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(5, 'red')
done()
print(22*10-9)