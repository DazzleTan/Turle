'''
使用嵌套循环绘制波形图
'''
import turtle as t
t.lt(90)
for i in range(0,6):
    for j in range(0,3):
        t.fd(30)
        t.rt(90)
    t.rt(180)
    t.fd(30)
    t.lt(90)
t.done()