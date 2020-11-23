'''
绘制小圆，外面均匀分布4个大圆
'''
import turtle as t
for i in range(0,3):
    for j in range(0,120):
        t.fd(0.0174*10)
        t.lt(1)
    for j in range(0,360):
        t.fd(0.0174*40)
        t.rt(1)
t.done()