'''
嵌套循环绘制连续的5个三角形
'''
import turtle as t
for i in range(0,5):
    for j in range(0,3):
        t.fd(50)
        t.lt(120)
    t.fd(50)
t.done()