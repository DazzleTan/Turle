'''
三个相互外切的圆
'''
import turtle as t
for i in range(0,3):
    t.rt(90)
    for j in range(0,360):
        t.fd(0.0174*50)
        t.lt(1)
    t.lt(90)
    t.pu()
    t.fd(50)
    t.lt(120)
    t.fd(50)
    t.pd()
t.done()