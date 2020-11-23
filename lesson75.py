'''
绘制立体五角星
'''
import turtle as t
t.hideturtle()
def ltwjx(s):
    for i in range(0,5):
        t.fd(s)
        t.rt(144)
        t.fd(s)
        t.rt(54)
        t.fd(s*1.9)
        t.bk(s*1.9)
        t.lt(126)
    return
 
ltwjx(50)

t.done()