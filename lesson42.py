'''
绘制8个角度一样的正方形
'''
import turtle as t
for i in range(0,8):
    for j in range(0,4):
        t.fd(80)
        t.lt(90)
    t.rt(45)
t.done()