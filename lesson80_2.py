'''
方法二
'''
import turtle as t
def yuanhu(r, n):
    t.circle(-r, n)
    return
 
def youquxian(r, n):
    for i in range(2):
        yuanhu(r, n)
        yuanhu(-r, n)
    return
 
def zuoquxian(r, n):
    for i in range(2):
        yuanhu(-r, n)
        yuanhu(r, n)
    return
 
t.rt(30)
for i in range(0, 9):
    youquxian(20, 100)
    t.rt(180-180/9)

t.done()