'''
使用嵌套循环绘制4个一样的三角形
'''
import turtle as t
for i in range(0,4):
    for j in range(0,3):
        t.fd(80)
        t.lt(120)
    t.rt(90)
t.done()