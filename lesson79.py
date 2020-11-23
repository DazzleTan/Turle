'''
绘制四叶莲花
'''
import turtle as t
t.hideturtle()
def yuanhu(r, n):
    # 用 循环绘制
    # for i in range(0,n):
    #     t.fd(0.0174*r)
    #     t.rt(1)
    # 用 circle 方法绘制
    t.circle(-r, n)
 
def yezi(r, n):
    for i in range(0,2):
        yuanhu(r,n)
        t.rt(180-n)
 
t.lt(90)
t.fd(50)
t.lt(90)
for i in range(0, 4):
    yezi(80, 90)
    t.rt(30)

t.done()