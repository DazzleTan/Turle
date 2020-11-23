'''
绘制由三段圆弧组成的逗号(方法一)
'''
import turtle as t
def rbanyuan(r):
    for i in range(0, 180):
        t.fd(0.0174*r)
        t.rt(1)
    return
 
def lbanyuan(r):
    for i in range(0, 180):
        t.fd(0.0174*r)
        t.lt(1)
    return
 
rbanyuan(50)
t.rt(180)
lbanyuan(100)
lbanyuan(50)
t.done()