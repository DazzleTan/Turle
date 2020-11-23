'''
使用circle()函数绘制3个互相外切的圆
'''
import turtle as t
for i in range(0,3):
    t.rt(90)
    t.circle(50)
    t.lt(90)
    t.pu()
    t.fd(50)
    t.lt(120)
    t.fd(50)
    t.pd()
t.done()