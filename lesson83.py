'''
绘制由圆和圆弧组成的图形
'''
import turtle as t
import math

t.hideturtle()

def yuanhu(r, n):
    # 用 循环绘制
    # for i in range(0,n):
    #     t.fd(0.0174*r)
    #     t.lt(1)
    # 用 circle 方法绘制
    t.circle(r, n)
 
r1=20
r2=48.3
# 计算
# r2=r1/(math.sqrt(2)-1)
 
# 绘制里面四个圆弧
for i in range(0,4):
    yuanhu(r1, 90)
    t.rt(180)
t.rt(90)
 
# 绘制里面圆
yuanhu(r1, 360)
 
# 移动位置
yuanhu(r1, 45)
yuanhu(-r2, 45)
 
# 绘制外面大圆
t.lt(90)
yuanhu(r2, 360)
 
# 绘制外面四条圆弧
t.lt(90)
for i in range(0,4):
    yuanhu(r2, 90)
    t.rt(180)
t.done()