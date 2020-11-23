'''
使用循环绘制楼梯形
'''
import turtle as t
t.lt(90)
for i in range(0,5):
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.lt(90)
t.done()