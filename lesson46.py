'''
使用嵌套循环绘制8叶长方形风车
'''
import turtle as t
for i in range(0,8):
    for j in range(0,2):
        t.fd(100)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.rt(45)
t.done()