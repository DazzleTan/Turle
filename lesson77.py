'''
使用三角形绘制蝴蝶
'''
import turtle as t
t.hideturtle()
def sjx(d):
    for i in range(0,3):
        t.fd(d)
        t.rt(120)
 
# 绘制左边的翅膀
t.lt(30)
s = 40
for i in range(0, 4):
    sjx(s)
    s = s + 10
 
# 绘制下方的三角形
s = 40
t.rt(90)
sjx(s)
 
# 绘制右边的翅膀
t.rt(90)
s = 40
for i in range(0, 4):
    sjx(s)
    s = s + 10
 
# 绘制两个触角
t.rt(90)
t.fd(60)
t.lt(120)
t.fd(10)
t.pu()
t.home()
t.pd()
t.lt(60)
t.fd(60)
t.rt(120)
t.fd(10)
t.done()