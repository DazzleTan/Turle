'''
使用嵌套循环绘制立体图
'''
import turtle as t
for i in range(0,3):
    t.pu()
    t.fd(50)
    t.pd()
    for j in range(0,3):
        for k in range(0,2):
            t.fd(50)
            t.rt(120)
            t.fd(50)
            t.rt(60)
        t.rt(120)
    t.pu()
    t.bk(50)
    t.rt(120)
t.done()