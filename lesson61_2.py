'''
使用circle()方法绘制五边形，每条边上一个小圆
'''
import turtle as t
for i in range(0,5):
    t.fd(100)
    t.rt(360/5)
    t.circle(10)
t.done()