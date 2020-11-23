'''
使用50和120，可以基本实现这种效果，
如果精确的两个长方形角重叠，需要使用勾股定理精确计算。
'''
import turtle as t
for i in range(0,2):
    t.fd(120)
    t.lt(90)
    t.fd(50)
    t.lt(90)
t.lt(45)
for i in range(0,2):
    t.fd(120)
    t.rt(90)
    t.fd(50)
    t.rt(90)
t.done()