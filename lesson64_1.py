'''
使用循环绘制伞
'''
import turtle as t
for i in range(0,90):
    t.fd(0.0174*30)
    t.rt(1)
t.lt(180)
for i in range(0,180):
    t.fd(0.0174*30)
    t.rt(1)
t.lt(180)
for i in range(0,180):
    t.fd(0.0174*90)
    t.lt(1)
t.lt(180)
for i in range(0,180):
    t.fd(0.0174*30)
    t.rt(1)
t.lt(180)
for i in range(0,90):
    t.fd(0.0174*30)
    t.rt(1)
t.rt(90)
t.fd(100)
for i in range(0,180):
    t.fd(0.0174*10)
    t.rt(1)
t.done()