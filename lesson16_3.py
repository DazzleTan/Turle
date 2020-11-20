'''
for...嵌套循环
'''
import turtle as t
for i in range(0,4):
    for i in range(0,3):
        t.fd(50)
        t.lt(90)
    t.rt(180)
t.done()