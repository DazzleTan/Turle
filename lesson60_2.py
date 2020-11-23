'''
使用circle()方法绘制小圆，外面均匀分布3个大圆
'''
import turtle as t
t.hideturtle()
for i in range(0,3):
    t.circle(10, 120)
    t.lt(180)
    t.circle(40)
    t.lt(180)
t.done()