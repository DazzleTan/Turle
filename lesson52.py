'''
使用循环绘制五边形，每个角加一个五角星
'''
import turtle as t
for i in range(0,5):
    t.fd(100)
    for j in range(0,5):
        t.fd(30)
        t.rt(144)
    t.rt(72)
t.done()