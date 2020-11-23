'''
使用嵌套循环绘制由4个长方形组成的正方形
'''
import turtle as t
for i in range(0,4):
    t.fd(30)
    for j in range(0,2):
        t.fd(50)
        t.rt(90)
        t.fd(80)
        t.rt(90)
    t.rt(90)
t.done()