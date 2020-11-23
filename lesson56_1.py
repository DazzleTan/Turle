'''
使用嵌套循环绘制4个圆形
'''
import turtle as t
for i in range(0,4):
    for j in range(0,360):
        t.fd(0.0174*50)
        t.rt(1)
    t.rt(90)
t.done()