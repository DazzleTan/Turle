'''
使用嵌套循环绘制十字相关的图形
'''
import turtle as t
for i in range(0,4):
    for j in range(0,5):
        t.fd(25)
        t.lt(90)
        t.fd(10)
        t.bk(20)
        t.fd(10)
        t.rt(90)
    t.bk(125)
    t.rt(90)
t.done()