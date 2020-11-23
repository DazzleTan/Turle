'''
绘制小火箭
'''
import turtle as t
# 完成下方底座和横线
t.fd(30)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(10)
t.rt(90)
t.bk(10)
t.fd(50)
 
# 开始画右侧平行四边形
t.rt(45)
t.fd(30)
t.lt(135)
t.fd(30)
t.lt(45)
t.fd(30)
t.lt(135)
t.fd(30)
 
#调整方向开始画火箭
t.lt(180)
t.fd(100)
t.lt(30)
t.fd(50)
t.lt(120)
t.fd(50)
t.lt(30)
t.fd(100)
 
# 开始画左侧平行四边形
t.rt(45)
t.fd(30)
t.rt(135)
t.fd(30)
t.rt(45)
t.fd(30)
t.rt(135)

t.done()