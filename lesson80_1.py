'''
绘制曲线九角星
'''
import turtle as t
t.hideturtle()
def youyuanhu(r, n):
    for i in range(0,n):
        t.fd(0.0174*r)
        t.rt(1)
    return
 
def zuoyuanhu(r, n):
    for i in range(0,n):
        t.fd(0.0174*r)
        t.lt(1)
    return
 
def youquxian(r, n):
    for i in range(2):
        youyuanhu(r, n)
        zuoyuanhu(r, n)
    return
 
def zuoquxian(r, n):
    for i in range(2):
        zuoyuanhu(r, n)
        youyuanhu(r, n)
    return
 
t.rt(30)
for i in range(0, 9):
    youquxian(20, 100)
    t.rt(180-180/9)

t.done()