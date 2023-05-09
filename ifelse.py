import turtle
import random

tao = turtle.Pen()
tao.pensize(8)
# tao.forward(100)

def Silium(x,y):
    tao.up()
    tao.goto(x,y)
    tao.down()
    for i in range(4):
        tao.forward(50)
        tao.left(90)

for i in range(10):
    x = random.randint(-300,300)
    y = random.randint(0,300)
    print(x,y)
    if y >= 200:
        tao.color('red')
    elif y >= 100:
        tao.color('#45321e')
    else:
        tao.color('green')
    Silium(x,y)


turtle.done() #ป้องกันการปิดโปรแกรม
