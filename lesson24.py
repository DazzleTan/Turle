'''
嵌套循环绘制十字+五角星
'''
import turtle as t
for i in range(0,4):
    t.fd(100)
    for j in range(0,5):
        t.fd(50)
        t.rt(144)
    t.bk(100)
    t.rt(90)
t.done()