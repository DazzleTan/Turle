'''
使用嵌套循环绘制四个小旗子
'''
import turtle as t
for i in range(0,4):
    t.lt(90)
    t.fd(60)
    for j in range(0,4):
        t.fd(40)
        t.rt(90)
    t.bk(60)
    t.rt(90)
    t.pu()
    t.fd(60)
    t.pd()
t.done()