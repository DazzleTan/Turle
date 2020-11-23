'''
使用嵌套循环绘制五个角度一样的三角形
'''
import turtle as t
for i in range(0,5):
    for j in range(0,3):
        t.fd(80)
        t.lt(120)
    t.rt(72)
t.done()