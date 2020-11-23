'''
绘制12叶菱形
'''
import turtle as t
for i in range(0,12):
    for j in range(0,2):
        t.fd(100)
        t.rt(60)
        t.fd(100)
        t.rt(120)
    t.rt(30)
t.done()