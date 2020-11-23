'''
使用嵌套循环绘制由4个相同大小的菱形组成的四叶风车
'''
import turtle as t
t.lt(30)
for i in range(0,4):
    for j in range(0,2):
        t.fd(100)
        t.rt(60)
        t.fd(100)
        t.rt(120)
    t.rt(90)
t.done()