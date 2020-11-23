'''
使用嵌套循环，绘制连续的五个三角形
'''
import turtle as t
for i in range(0,5):
    for j in range(0,4):
        t.fd(50)
        t.lt(120)
    t.rt(120)
t.done()