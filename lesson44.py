'''
使用嵌套循环绘制4个长方形
'''
import turtle as t
for i in range(0,4):
    for j in range(0,2):
        t.fd(100)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.rt(90)
t.done()