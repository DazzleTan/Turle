'''
绘制依次增加的正方形
'''
import turtle as t
s = 10
for i in range(0, 13):
    t.fd(s)
    t.rt(90)
    s = s + 10
t.done()