'''
使用循环绘制长方形中的正方形
'''
import turtle as t
for i in range(0,2):
    t.fd(140)
    t.lt(90)
    t.fd(80)
    t.lt(90)
t.pu()
t.fd(50)
t.lt(90)
t.fd(20)
t.pd()
for i in range(0,4):
    t.fd(40)
    t.rt(90)
t.done()