'''
绘制五角星，每个角上有一个小圆
'''
import turtle as t
for i in range(0,5):
    t.fd(100)
    t.rt(144)
    for i in range(0,360):
        t.fd(0.0174*10)
        t.lt(1)
t.done()