'''
由圆和圆弧组成的蝴蝶
'''
import turtle as t

t.hideturtle()

def youyuanhu(r, n):
    # 用 循环绘制
    # for i in range(0,n):
    #     t.fd(0.0174*r)
    #     t.rt(1)
    # 用 circle 方法绘制
    t.circle(-r, n)
 
def zuoyuanhu(r, n):
    # 用 循环绘制
    # for i in range(0,n):
    #     t.fd(0.0174*r)
    #     t.lt(1)
    # 用 circle 方法绘制
    t.circle(r, n)
 
t.lt(90)
zuoyuanhu(10, 360)
zuoyuanhu(20, 360)
youyuanhu(10, 360)
youyuanhu(20, 360)
 
t.fd(80)
zuoyuanhu(20, 360)
zuoyuanhu(40, 360)
youyuanhu(20, 360)
youyuanhu(40, 360)
 
t.fd(50)
zuoyuanhu(20, 90)
zuoyuanhu(10, 360)
t.lt(180)
youyuanhu(20, 90)
t.lt(180)
youyuanhu(20, 90)
youyuanhu(10, 360)
t.done()