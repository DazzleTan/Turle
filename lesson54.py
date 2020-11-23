'''
使用嵌套循环绘制八个正方形图形
'''
import turtle as t
for i in range(0,4):
    for j in range(0,2):
        t.fd(50)
        t.rt(90)
    t.lt(90)
    for j in range(0,4):
        t.fd(50)
        t.lt(90)
    t.rt(90)
    for j in range(0,2):
        t.fd(50)
        t.rt(90)
    t.rt(90)
t.done()