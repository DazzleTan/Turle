'''
使用circle()函数绘制一个大圆，然后在外面均匀分布4个小圆
'''
import turtle as t
for i in range(0,4):
    t.circle(50,90)
    t.lt(180)
    t.circle(10)
    t.lt(180)
t.done()