'''
绘制正方形，正方形内有四叶草
'''
import turtle as t
for i in range(0,4):
    t.fd(100)
    t.lt(90)
    for j in range(0,180):
        t.fd(0.0174*50)
        t.lt(1)
    t.lt(90)
    t.fd(100)
    t.lt(90)
t.done()