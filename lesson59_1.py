'''
使用循环绘制一个大圆，然后再外面均匀分布4个小圆
'''
import turtle as t
for i in range(0,4):
    for j in range(0,90):
        t.fd(0.0174*50)
        t.lt(1)
    for j in range(0,360):
        t.fd(0.0174*10)
        t.rt(1)
t.done()