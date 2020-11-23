'''
使用circle()方法绘制五角星，每个角上有一个小圆
'''
import turtle as t
for i in range(0,5):
    t.fd(100)
    t.rt(144)
    t.circle(10)
t.done()