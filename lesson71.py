'''
绘制6个枝叶
'''
import turtle as t
def zhi():
    for i in range(0,2):
        t.fd(30)
        t.lt(30)
        t.fd(10)
        t.bk(10)
        t.rt(60)
        t.fd(10)
        t.bk(10)
        t.lt(30)
    t.fd(30)
    t.rt(30)
    for i in range(0,2):
        t.fd(10)
        t.lt(60)
        t.fd(10)
        t.lt(120)
    t.lt(30)
    t.bk(90)
    return
 
t.lt(90)
for i in range(0,6):
    zhi()
    t.rt(60)
t.done()