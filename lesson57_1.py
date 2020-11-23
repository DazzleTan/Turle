'''
使用循环绘制三角形和半圆
'''
import turtle as t
t.fd(100)
t.lt(90)
t.fd(140)
t.home()
t.lt(90)
for i in range(0,180):
    t.fd(0.0174*50)
    t.rt(1)
t.rt(90)
for i in range(0,180):
    t.fd(0.0174*70)
    t.rt(1)
t.done()