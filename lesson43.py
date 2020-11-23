'''
使用嵌套循环绘制6个小旗子
'''
import turtle as t
for i in range(0,6):
    t.fd(100)
    for j in range(0,4):
        t.fd(50)
        t.rt(90)
    t.bk(100)
    t.rt(60)
t.done()