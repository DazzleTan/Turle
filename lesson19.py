'''
使用for...循环绘制正六边形
'''
import turtle as t
for i in range(0, 6):
    t.fd(80)
    t.rt(360/6)
t.done()