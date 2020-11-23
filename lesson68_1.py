'''
绘制多个圆形
'''
import turtle as t
s=40
for i in range(0,5):
    for i in range(0, 360):
        t.fd(0.0174*s)
        t.lt(1)
    s=s+10
t.done()