'''
使用嵌套循环绘制由6个相同大小菱形组成的6叶风车
'''
import turtle as t
for i in range(0,6):
    for j in range(0,2):
        t.fd(100)
        t.rt(60)
        t.fd(100)
        t.rt(120)
    t.rt(60)
t.done()