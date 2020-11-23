'''
绘制8叶菱形风车
'''
import turtle as t
t.lt(30)
for i in range(0,8):
    for j in range(0,2):
        t.fd(100)
        t.rt(60)
        t.fd(100)
        t.rt(120)
    t.rt(45)
t.done()