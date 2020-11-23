'''
使用嵌套循环绘制三个角度一样的三角形
'''
import turtle as t
for i in range(0,3):
    for j in range(0,3):
        t.fd(80)
        t.lt(120)
    t.rt(120)
t.done()