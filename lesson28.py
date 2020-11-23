'''
使用循环绘制多条斜线（平行线）
'''
import turtle as t
for i in range(0,10):
    t.lt(60)
    t.fd(100)
    t.bk(100)
    t.rt(60)
    t.pu()
    t.fd(10)
    t.pd()
t.done()