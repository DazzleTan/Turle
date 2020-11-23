'''
使用嵌套循环绘制五个大小一样的正方形
'''
import turtle as t
for i in range(0,5):
    for j in range(0,4):
        t.fd(80)
        t.lt(90)
    t.rt(72)
t.done()