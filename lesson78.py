'''
绘制由半圆组成的梅花
'''
import turtle as t
def meihua(n, d):
    for i in range(0, n):
        t.circle(-d, 180)
        t.lt(180-360/n)
    return
t.lt(90)
meihua(3, 40)
t.done()