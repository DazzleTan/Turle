'''
每个正方形的长度依次增加20
'''
import turtle as t
s = 40
for i in range(0, 5):
    for j in range(0, 4):
        t.fd(s)
        t.lt(90)
    t.pu()
    t.bk(10)
    t.lt(90)
    t.bk(10)
    t.rt(90)
    t.pd()
    s=s+20
t.done()