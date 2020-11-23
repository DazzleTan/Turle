'''
绘制由圆弧组成的多边形
'''
import turtle as t
import math
def yuanhu(r, n):
    # 用 循环绘制
    # for i in range(0,n):
    #     t.fd(0.0174*r)
    #     t.lt(1)
    # 用 circle 方法绘制
    t.circle(r, n)
 
r=40
n=6
m=120
 
for i in range(0, n):
    # 计算使用
    # print(r*math.sin(math.radians(m/2))*2)
    t.fd(69.3)
    t.rt(360/n)
 
t.rt(90-(180-m)/2)
for i in range(0, n):
    yuanhu(r, m)
    t.rt(m)
    t.rt(360/n)
t.done()